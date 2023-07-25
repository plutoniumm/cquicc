"""SCPI access to Red Pitaya."""
import socket
import struct

__author__ = "Luka Golinar, Iztok Jeras, Miha Gjura"
__copyright__ = "Copyright 2023, Red Pitaya"

class scpi (object):
    """SCPI class used to access Red Pitaya over an IP network."""
    delimiter = '\r\n'

    def __init__(self, host, timeout=None, port=5000):
        """Initialize object and open IP connection.
        Host IP should be a string in parentheses, like '192.168.1.100'.
        """
        self.host    = host
        self.port    = port
        self.timeout = timeout

        try:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            if timeout is not None:
                self._socket.settimeout(timeout)

            self._socket.connect((host, port))

        except socket.error as e:
            print('SCPI >> connect({!s:s}:{:d}) failed: {!s:s}'.format(host, port, e))

    def __del__(self):
        if self._socket is not None:
            self._socket.close()
        self._socket = None

    def close(self):
        """Close IP connection."""
        self.__del__()

    def rx_txt(self, chunksize = 4096):
        """Receive text string and return it after removing the delimiter."""
        msg = ''
        while 1:
            chunk = self._socket.recv(chunksize).decode('utf-8') # Receive chunk size of 2^n preferably
            msg += chunk
            if (len(msg) and msg[-2:] == self.delimiter):
                break
        return msg[:-2]

    def rx_arb(self):
        """ Recieve binary data from scpi server"""
        numOfBytes = 0
        data=b''
        while len(data) != 1:
            data = self._socket.recv(1)
        if data != b'#':
            return False
        data=b''
        while len(data) != 1:
            data = self._socket.recv(1)
        numOfNumBytes = int(data)
        if numOfNumBytes <= 0:
            return False
        data=b''
        while len(data) != numOfNumBytes:
            data += (self._socket.recv(1))
        numOfBytes = int(data)
        data=b''
        while len(data) != numOfBytes:
            data += (self._socket.recv(4096))
        return data

    def tx_txt(self, msg):
        """Send text string ending and append delimiter."""
        return self._socket.sendall((msg + self.delimiter).encode('utf-8')) # was send(().encode('utf-8'))

    def txrx_txt(self, msg):
        """Send/receive text string."""
        self.tx_txt(msg)
        return self.rx_txt()


# SCPI command functions
    def sour_set(
        self,
        chan: int,
        func: str = "sine",
        volt: float = 1,
        freq: float = 1000,
        offset: float = 0,
        phase: float = 0,
        dcyc: float = 0.5,
        data = None,
        burst: bool = False,
        ncyc: int = 1,
        nor: int = 1,
        period: int = None,
        trig: str = "int",
        sdrlab: bool = False,
        siglab: bool = False,
    ) -> None:

        """
        Set the parameters for signal generator on one channel.

        Parameters
        -----------
            chan (int) :
                Output channel (either 1 or 2).
            func (str, optional) :
                Waveform of the signal (SINE, SQUARE, TRIANGLE, SAWU,
                SAWD, PWM, ARBITRARY, DC, DC_NEG).
                Defaults to `sine`.
            volt (int, optional) :
                Amplitude of signal {-1, 1} Volts. {-5, 5} for SIGNALlab 250-12.
                Defaults to 1.
            freq (int, optional) :
                Frequency of signal. Not relevant if 'func' is "DC" or "DC_NEG".
                Defaults to 1000.
            offset (int, optional) :
                Signal offset {-1, 1} Volts. {-5, 5} for SIGNALlab 250-12.
                Defaults to 0.
            phase (int, optional) :
                Phase of signal {-360, 360} degrees.
                Defaults to 0.
            dcyc (float, optional) :
                Duty cycle, where 1 corresponds to 100%.
                Defaults to 0.5.
            data (ndarray, optional) :
                Numpy ``ndarray`` of max 16384 values, floats in range {-1,1}
                (or {-5,5} for SIGNALlab).
                Define the custom waveform if "func" is "ARBITRARY".
                Defaults to `None`.
            burst (bool, optional) :
                Enable/disable Burst mode. (`True` - BURST, `False` - CONINUOUS)
                Generate "nor" number of "ncyc" periods with total time "period".
                Defaults to `False`.
            ncyc (int, optional) :
                Number of periods in one burst.
                Defaults to 1.
            nor (int, optional) :
                Number of repeated bursts.
                Defaults to 1.
            period (_type_, optional) :
                Total time of one burst in µs {1, 5e8}. Includes the signal and delay.
                Defaults to `None`.
            trig (str, optional):
                Trigger source (EXT_PE, EXT_NE, INT, GATED).
                Defaults to `int` (internal).
            sdrlab (bool, optional):
                `True` if operating with SDRlab 122-16.
                Defaults to `False`.
            siglab (bool, optional):
                `True` if operating with SIGNALlab 250-12.
                Defaults to `False`.

        The settings will work on any Red Pitaya board. If operating on a board
        other than STEMlab 125-14, change the bool value of the appropriate
        parameter to true (sdrlab, siglab)

        Raises
        ------

        Raises errors if the input parameters are out of range.

        """

        ### Constants ###
        waveform_list = ["SINE","SQUARE","TRIANGLE","SAWU","SAWD","PWM","ARBITRARY","DC","DC_NEG"]
        trigger_list = ["EXT_PE","EXT_NE","INT","GATED"]
        buff_size = 16384

        ### Limits ###
        volt_lim = 1
        offs_lim = 1
        phase_lim = 360
        freq_up_lim = 50e6          # 50 MHz
        freq_down_lim = 0

        if siglab:
            volt_lim = 5
            offs_lim = 5
        elif sdrlab:
            freq_down_lim = 300e3   # 300 kHz



        ### CHECK FOR ERRORS ###

        try:
            assert chan in (1,2)
        except AssertionError as channel_err:
            raise ValueError("Channel needs to be either 1 or 2") from channel_err

        try:
            assert func.upper() in waveform_list
        except AssertionError as waveform_err:
            print(func.upper(), "is not a defined waveform")

        try:
            assert freq_down_lim < freq <= freq_up_lim
        except AssertionError as freq_err:
            print("Frequency out of range", freq_down_lim, freq_up_lim)

        try:
            assert abs(volt) <= volt_lim
        except AssertionError as ampl_err:
            print("Amplitude out of range", -volt_lim, volt_lim)

        try:
            assert abs(offset) <= offs_lim
        except AssertionError as offs_err:
            print("Offset out of range", -offs_lim, offs_lim)

        try:
            assert 0 <= dcyc <= 1
        except AssertionError as dcyc_err:
            print("Duty cycle out of range", 0, 1)

        try:
            assert abs(phase) <= phase_lim
        except AssertionError as phase_err:
            print("Phase out of range", -phase_lim, phase_lim)

        if data is not None:

            try:
                assert data.shape[0] <= buff_size
            except AssertionError as data_err:
                print("Data length out of range. Max: ", buff_size)

        try:
            assert ncyc >= 1
        except AssertionError as ncyc_err:
            print("NCYC minimum is 1")

        try:
            assert nor >= 1
        except AssertionError as nor_err:
            print("NOR minimum is 1")

        if period is not None:
            try:
                assert period >= 1
            except AssertionError as period_err:
                print("Period needs to be greater than 1 µs")

        try:
            assert trig.upper() in trigger_list
        except AssertionError as trig_err:
            print(trig.upper(), "is not a defined trigger source")

        try:
            assert not((siglab is True) and (sdrlab is True))
        except AssertionError as board_err:
            print("Please select only one board option. 'siglab' and 'sdrlab' cannot be true at the same time.")



        ### Variables ###
        wf_data = []


        ### SEND COMMANDS TO RP ###
        self.tx_txt("SOUR{0}:FUNC {1}".format(chan, func.upper()))
        self.tx_txt("SOUR{0}:VOLT {1}".format(chan, volt))

        if func.upper() not in waveform_list[7:9]:
            self.tx_txt("SOUR{0}:FREQ:FIX {1}".format(chan, freq))

        self.tx_txt("SOUR{0}:VOLT:OFFS {1}".format(chan, offset))
        self.tx_txt("SOUR{0}:PHAS {1}".format(chan, phase))

        if func.upper() == "PWM":
            self.tx_txt("SOUR{0}:DCYC {1}".format(chan, dcyc))

        if (data is not None) and (func.upper() == "ARBITRARY"):
            wf_data = []
            for n in data:
                wf_data.append("{:.5f}".format(n))
            cust_wf = ", ".join(map(str, wf_data))

            self.tx_txt("SOUR{0}:TRAC:DATA:DATA {1}".format(chan, cust_wf))

        if burst:
            self.tx_txt("SOUR{0}:BURS:STAT BURST".format(chan))
            self.tx_txt("SOUR{0}:BURS:NCYC {1}".format(chan, ncyc))
            self.tx_txt("SOUR{0}:BURS:NOR {1}".format(chan, nor))

            if period is not None:
                self.tx_txt("SOUR{0}:BURS:INT:PER {1}".format(chan, period))
        else:
            self.tx_txt("SOUR{0}:BURS:STAT CONTINUOUS".format(chan))

        self.tx_txt("SOUR{0}:TRIG:SOUR {1}".format(chan, trig.upper()))


    def acq_set(
        self,
        dec: int = 1,
        trig_lvl: float = 0,
        trig_delay: int = 0,
        trig_delay_ns: bool = False,
        units: str = None,
        sample_format: str = None,
        averaging: bool = True,
        gain: list = None,               # 2 channels (double the length if 4-input)
        coupling: list = None,           # 2 channels
        ext_trig_lvl: float = 0,
        siglab: bool = False,
        input4: bool = False
    ) -> None:

        """

        Set the parameters for signal acquisition.

        Parameters
        -----------

            dec (int, optional) :
                Decimation (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048,
                4096, 8192, 16384, 32768, 65536)
                Defaults to 1.
            trig_lvl (float, optional) :
                Trigger level in Volts. {-1, 1} Volts on LV gain or {-20, 20} Volts on HV gain.
                Defaults to 0.
            trig_delay (int, optional) :
                Trigger delay in samples (if trig_delay_ns = True, then the delay is in ns)
                Defaults to 0.
            trig_delay_ns (bool, optional) :
                Change the trigger delay to nanoseconds instead of samples.
                Defaults to False.
            units (str, optional) :
                The units in which the acquired data will be returned.
                Defaults to "VOLTS".
            sample_format (str, optional) :
                The format in which the acquired data will be returned.
                Defaults to "ASCII".
            averaging (bool, optional) :
                Enable/disable averaging. When True, if decimation is higher than 1,
                each returned sample is the average of the taken samples. For example,
                if dec = 4, the returned sample will be the average of the 4 decimated
                samples.
                Defaults to True.
            gain (list(str), optional) :
                HV / LV - (High (1:20) or Low (1:1 attenuation))
                The first element in list applies to the SOUR1 and the second to SOUR2.
                Refers to jumper settings on Red Pitaya fast analog inputs.
                (1:20 and 1:1 attenuator for SIGNALlab 250-12)
                Defaults to ["LV","LV"].
            coupling (list(str), optional) :
                AC / DC - coupling mode for fast analog inputs.
                The first element in list applies to the SOUR1 and the second to SOUR2.
                (Only SIGNALlab 250-12)
                Defaults to ["DC","DC"].
            ext_trig_lvl (float, optional) :
                Set trigger external level in V.
                (Only SIGNALlab 250-12)
                Defaults to 0.
            siglab (bool, optional) :
                Set to True if operating with SIGNALlab 250-12.
                Defaults to False.
            input4 (bool, optional) :
                Set to True if operating with STEMlab 125-14 4-Input.
                Defaults to False.

        The settings will work on any Red Pitaya board. If operating on SIGNALlab 250-12
        or STEMlab 125-14 4-Input change the bool value of the appropriate parameter to
        true (siglab, input4). This will change the available range of input parameters.

        Raises
        ------

            Raises errors if the input parameters are out of range.

        """

        ### Constants ###
        #decimation_list = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536]
        gain_list = ["LV","HV"]
        coupling_list = ["DC","AC"]
        units_list = ["RAW","VOLTS"]
        format_list = ["BIN", "ASCII"]

        ### Limits ###
        if input4:   # Set number of channels
            n = 4
        else:
            n = 2
        trig_lvl_lim = 1.0
        gain_lvl = "LV"

        if gain is not None:
            for i in gain:
                if i.upper() == "HV":
                    trig_lvl_lim = 20.0
                    gain_lvl = "HV"

        try:
            assert abs(trig_lvl) <= trig_lvl_lim
        except AssertionError as trig_err:
            print("Trigger level out of range", -trig_lvl_lim, trig_lvl_lim, "V for gain", gain_lvl)

        try:
            assert trig_delay >= 0
        except AssertionError as trig_dly_err:
            print("Trigger delay needs to be greater than 0")

        if units is not None:
            try:
                assert units.upper() in units_list
            except AssertionError as unit_err:
                print(units.upper(), "is not a defined unit")

        if sample_format is not None:
            try:
                assert sample_format.upper() in format_list
            except AssertionError as format_err:
                print(sample_format.upper(), "is not a defined format")

        if gain is not None:
            try:
                assert (gain[0].upper() in gain_list) and (gain[1].upper() in gain_list)
            except AssertionError as gain_err:
                print(gain[0].upper(), "or", gain[1].upper(), "is not a defined gain")

        if siglab and coupling is not None:
            try:
                assert (coupling[0].upper() in coupling_list) and (coupling[1].upper() in coupling_list)
            except AssertionError as coupling_err:
                print(coupling[0].upper(), "or", coupling[1].upper(), "is not a defined coupling")
            try:
                assert abs(ext_trig_lvl) <= trig_lvl_lim
            except AssertionError as ext_trig_err:
                print("External trigger level out of range", -trig_lvl_lim, trig_lvl_lim, "V")

        try:
            assert not((siglab is True) and (input4 is True))
        except AssertionError as board_err:
            print("Please select only one board option. 'siglab' and 'input4' cannot be true at the same time.")


        ### SEND COMMANDS TO RP ###
        self.tx_txt("ACQ:DEC {}".format(dec))

        if averaging:
            self.tx_txt("ACQ:AVG ON")
        else:
            self.tx_txt("ACQ:AVG OFF")

        if trig_delay_ns:
            self.tx_txt("ACQ:TRIG:DLY:NS {}".format(trig_delay))
        else:
            self.tx_txt("ACQ:TRIG:DLY {}".format(trig_delay))

        if units is not None:
            self.tx_txt("ACQ:DATA:UNITS {}".format(units.upper()))
        if sample_format is not None:
            self.tx_txt("ACQ:DATA:FORMAT {}".format(sample_format.upper()))

        if gain is not None:
            for i in range(n):
                self.tx_txt("ACQ:SOUR{}:GAIN {}".format(i + 1, gain[i].upper()))

        self.tx_txt("ACQ:TRIG:LEV {}".format(trig_lvl))

        if siglab and coupling is not None:
            for i in range(n):
                self.tx_txt("ACQ:SOUR{}:COUP {}".format(i + 1, coupling[i].upper()))

            self.tx_txt("ACQ:TRIG:EXT:LEV {}".format(ext_trig_lvl))


        #print("ACQ set successfully")

    def get_settings(
        self,
        siglab: bool = False,
        input4: bool = False
    ) -> str:
        """

        Retrieves the settings from Red Pitaya, prints them in console and returns
        them as an array with the following sequence:
        [decimation, avearge, trig_dly, trig_dly_ns, trig_lvl, buf_size, gain_ch1, gain_ch2, coup_ch1, coup_ch2, ext_trig_lvl]
                                                                                           , gain_ch3, gain_ch4
            Decimation   - Current decimation
            Average      - Current averaging status (ON/OFF)
            Trig_dly     - Current trigger delay in samples
            Trig_dly_ns  - Current trigger delay in nanoseconds
            Trig_lvl     - Current triger level in Volts
            Buf_size     - Buffer size
            Gain_ch1-4   - Current gain on channels (CH3 and CH4 STEMlab 125-14 4-Input only)
            Coup_ch1/2   - Current coupling mode for both channels (AC/DC) (SIGNALlab only)
            Ext_trig_lvl - Current external trigger level in Volts (SIGNALlab only)

        Note:   The last three array elements won't exist if siglab = False
                Gain of channels 3 and 4 only if input4 = True

        Parameters
        ----------
            siglab (bool, optional):
                Set to True if operating with SIGNALlab 250-12.
                Defaults to False.
            input4 (bool, optional):
                Set to True if operating with STEMlab 125-14 4-Input.
                Defaults to False.

        """

        try:
            assert not((siglab is True) and (input4 is True))
        except AssertionError as board_err:
            raise ValueError("Please select only one board option. 'siglab' and 'input4' cannot be true at the same time.") from board_err


        settings = []

        if input4:   # Set number of channels
            n = 4
        else:
            n = 2

        settings.append(self.txrx_txt("ACQ:DEC?"))
        settings.append(self.txrx_txt("ACQ:AVG?"))
        settings.append(self.txrx_txt("ACQ:TRIG:DLY?"))
        settings.append(self.txrx_txt("ACQ:TRIG:DLY:NS?"))
        settings.append(self.txrx_txt("ACQ:TRIG:LEV?"))
        settings.append(self.txrx_txt("ACQ:BUF:SIZE?"))

        for i in range(n):
            settings.append(self.txrx_txt("ACQ:SOUR{}:GAIN?".format(i+1)))

        if siglab:
            for i in range(2):
                settings.append(self.txrx_txt("ACQ:SOUR{}:COUP?".format(i+1)))

            settings.append(self.txrx_txt("ACQ:TRIG:EXT:LEV?"))

        print("Decimation: {}".format(settings[0]))
        print("Averaging: {}".format(settings[1]))
        print("Trigger delay (samples): {}".format(settings[2]))
        print("Trigger delay (ns): {}".format(settings[3]))
        print("Trigger level (V): {}".format(settings[4]))
        print("Buffer size: {}".format(settings[5]))

        if input4:
            print("Gain CH1/CH2/CH3/CH4: {}, {}, {}, {}".format(settings[6], settings[7], settings[8], settings[9]))
        else:
            print("Gain CH1/CH2: {}, {}".format(settings[6], settings[7]))

        if siglab:
            print("Coupling CH1/CH2: {}, {}".format(settings[8], settings[9]))
            print("External trigger level (V): {}".format(settings[10]))

        return settings


    def acq_data(
        self,
        chan: int,
        start: int = None,
        end: int = None,
        num_samples: int = None,
        old: bool = False,
        lat: bool = False,
        binary: bool = False,
        convert: bool = False,
        input4: bool = False
    ) -> list:
        """
        Returns the acquired data on a channel from the Red Pitaya, with the following options (for a specific channel):
            - only channel       => returns the whole buffer
            - start and end      => returns the samples between them
            - start and n        => returns 'n' samples from the start position
            - old and n          => returns 'n' oldest samples in the buffer
            - lat and n          => returns 'n' latest samples in the buffer

        Parameters
        ----------
            chan (int) :
                Input channel (either 1 or 2).
                (1-4 for STEMlab 125-14 4-Input)
            start (int, optional):
                Start position of acquired data in the buffer {0,1,...16384}
                Defaults to None.
            end (int, optional):
                End position of acquired data in the buffer {0,1,...16384}
                Defaults to None.
            n (int, optional):
                Number of samples read.
            old (bool, optional):
                Read oldest samples in the buffer.
            lat (bool, optional):
                Read latest samples in the buffer.
            bin (bool, optional):
                Set to True if working with Binary data.
                Defaults to False.
            convert (bool, optional):
                Set to True to convert data to a list of floats (VOLTS) or integers (RAW).
                Otherwise returns a list of str (VOLTS) or int (RAW).
                Defaults to False.
            input4 (bool, optional) :
                Set to True if operating with STEMlab 125-14 4-Input.
                Defaults to False.


        Raises
        ------

            Raises errors if the input parameters do not match one of the options.

        """

        low_lim = 0
        up_lim = 16384

        # Check input data for errors
        if input4:
            try:
                assert chan in (1,2,3,4)
            except AssertionError as chanel_err:
                raise ValueError("Channel needs to be either 1, 2, 3 or 4") from chanel_err
        else:
            try:
                assert chan in (1,2)
            except AssertionError as chanel_err:
                raise ValueError("Channel needs to be either 1 or 2") from chanel_err

        try:
            assert not((old is True) and (lat is True))
        except AssertionError as arg_err:
            raise ValueError("Please select only one. 'old' and 'lat' cannot be True at the same time.") from arg_err

        if start is not None:
            try:
                assert 16384 >= start >= 0
            except AssertionError as start_err:
                print("Start position out of range", low_lim, up_lim)

        if end is not None:
            try:
                assert 16384 >= end >= 0
            except AssertionError as end_err:
                print("End position out of range", low_lim, up_lim)

        if num_samples is not None:
            try:
                assert 16384 >= num_samples >= 0
            except AssertionError as sample_err:
                print("Number of samples out of range", low_lim, up_lim)

        # Get data type from Red Pitaya
        units = self.txrx_txt('ACQ:DATA:UNITS?')
        # format = self.txrx_txt("ACQ:DATA:FORMAT?")


        # Determine the output data
        if (start is not None) and (end is not None):
            self.tx_txt("ACQ:SOUR{}:DATA:STA:END? {},{}".format(chan, start, end))
        elif (start is not None) and (num_samples is not None):
            self.tx_txt("ACQ:SOUR{}:DATA:STA:N? {},{}".format(chan, start, num_samples))
        elif old and (num_samples is not None):
            self.tx_txt("ACQ:SOUR{}:DATA:OLD:N? {}".format(chan, num_samples))
        elif lat and (num_samples is not None):
            self.tx_txt("ACQ:SOUR{}:DATA:LAT:N? {}".format(chan, num_samples))
        else:
            self.tx_txt("ACQ:SOUR{}:DATA?".format(chan))


        # Convert data
        if binary:
            buff_byte = self.rx_arb()

            if convert:
                if units == "VOLTS":
                    buff = [struct.unpack('!f',bytearray(buff_byte[i:i+4]))[0] for i in range(0, len(buff_byte), 4)]
                elif units == "RAW":
                    buff = [struct.unpack('!h',bytearray(buff_byte[i:i+2]))[0] for i in range(0, len(buff_byte), 2)]
            else:
                buff = buff_byte
        else:
            buff_string = self.rx_txt()

            if convert:
                buff_string = buff_string.strip('{}\n\r').replace("  ", "").split(',')
                buff = list(map(float, buff_string))
            else:
                buff = buff_string

        return buff


    def uart_set(
        self,
        speed: int = 9600,
        bits: str = "CS8",
        parity: str = "NONE",
        stop: int = 1,
        timeout: int = 0
    ) -> None:
        """
        Configures the provided settings for UART.

        Args:
            speed (int, optional): Baud rate/speed of UART connection (bits per second). Defaults to 9600.
            bits (str, optional): Character size in bits (CS6, CS7, CS8). Defaults to "CS8".
            parity (str, optional): Parity (NONE, EVEN, ODD, MARK, SPACE). Defaults to "NONE".
            stop (int, optional): Number of stop bits (1 or 2). Defaults to 1.
            timeout (int, optional): Timeout for reading from UART (in 1/10 of seconds) {0,...255}. Defaults to 0.
        """

        # Constants
        speed_list = [1200,2400,4800,9600,19200,38400,57600,115200,230400,576000,921000,1000000,1152000,1500000,2000000,2500000,3000000,3500000,4000000]
        database_list = ["CS6","CS7","CS8"]
        parity_list = ["NONE","EVEN","ODD","MARK","SPACE"]


        # Input Limits Check
        try:
            assert speed in speed_list
        except AssertionError as speed_err:
            print(speed, "is not a defined speed for UART connection. Please check the speed table.")

        try:
            assert bits in database_list
        except AssertionError as bits_err:
            print(bits, "is not a defined character size.")

        try:
            assert parity in parity_list
        except AssertionError as parity_err:
            print(parity, "is not a defined parity.")

        try:
            assert stop in (1,2)
        except AssertionError as stop_err:
            print("The number of stop bits can only be 1 or 2")

        try:
            assert 0 <= timeout <= 255
        except AssertionError as timeout_err:
            print("Timeout out of range. Please select a value between 0 and 255.")

        # Configuring UART

        self.tx_txt("UART:INIT")
        self.tx_txt("UART:SPEED {}".format(speed))
        self.tx_txt("UART:BITS {}".format(bits.upper()))
        self.tx_txt("UART:STOPB STOP{}".format(stop))
        self.tx_txt("UART:PARITY {}".format(parity.upper()))
        self.tx_txt("UART:TIMEOUT {}".format(timeout))


        self.tx_txt("UART:SETUP")
        print("UART is configured")

    def uart_get_settings(
        self
    ) -> str:
        """
        Retrieves the settings from Red Pitaya, prints them in console and returns
        them as an array with the following sequence:
        [speed, databits, stopbits, parity, timeout]

        """

        settings = []

        settings.append(self.txrx_txt("UART:SPEED?"))
        settings.append(self.txrx_txt("UART:BITS?"))

        stop = self.txrx_txt("UART:STOPB?")
        if stop == "STOP1":
            settings.append("1")
        elif stop == "STOP2":
            settings.append("2")

        settings.append(self.txrx_txt("UART:PARITY?"))
        settings.append(self.txrx_txt("UART:TIMEOUT?"))


        print("Baudrate/Speed: {}".format(settings[0]))
        print("Databits: {}".format(settings[1]))
        print("Stopbits: {}".format(settings[2]))
        print("Parity: {}".format(settings[3]))
        print("Timeout (0.1 sec): {}".format(settings[4]))

        return settings

    def uart_write_string(
        self,
        string: str,
        word_length: bool = False
    ) -> None:
        """
        Sends a string of characters through UART.

        Args:
            string (str, optional): String that will be sent.
            word_length (bool, optional): Set to True if UART word lenght is set to 7 (ASCII) or
                                    False if UART word length is set to 8 (UTF-8). Defaults to False.
        """

        if word_length:
            # word length 7 / ASCII
            code = "ascii"
        else:
            # word length 8 / UTF-8
            code = "utf-8"


        # transforming and writing to UART
        arr = ',#H'.join('{:X}'.format(x) for x in bytearray(string, '{}'.format(code)))
        self.tx_txt('UART:WRITE{} #H{}'.format(len(string), arr))

        print("String sent")

    def uart_read_string(
        self,
        length: int
    ) -> str:
        """
        Reads a string of data from UART and decodes it from ASCII to string.

        Args:
            length (int): Length of data to read from UART.

        Returns:
            str: Read data in string format.
        """

        # Check for errors
        try:
            assert length > 0
        except AssertionError as length_err:
            raise ValueError("Length must be greater than 0.") from length_err

        self.tx_txt("UART:READ{}".format(length))
        res = self.rx_txt()
        res = res.strip('{}\n\r').replace("  ", "").split(',')
        string = "".join(chr(int(x)) for x in res)  # int(x).decode("utf8")

        return string


    def spi_set(
        self,
        spi_mode: str = None,
        cs_mode: str = None,
        speed: int = None,
        word_len: int = None
    ) -> None:
        """
        Configures the provided settings for SPI.

        Args:
            spi_mode (str, optional): Sets the mode for SPI; - LISL (Low Idle level, Sample Leading edge)
                                                             - LIST (Low Idle level, Sample Trailing edge)
                                                             - HISL (High Idle level, Sample Leading edge)
                                                             - HIST (High Idle level, Sample Trailing edge)
                                                        Defaults to LISL.
            cs_mode (str, optional): Sets the mode for CS: - NORMAL (After message transmission, CS => HIGH)
                                                           - HIGH (After message transmission, CS => LOW)
                                                        Defaults to NORMAL.
            speed (int, optional): Sets the speed of the SPI connection. Defaults to 5e7.
            word_len (int, optional): Character size in bits (CS6, CS7, CS8). Defaults to "CS8".
        """

        # Constants
        speed_max_limit = 100e6
        speed_min_limit = 1
        cs_mode_list = ["NORMAL","HIGH"]
        order_list = ["MSB","LSB"]
        spi_mode_list = ["LISL","LIST","HISL","HIST"]
        bits_min_limit = 7


        # Input Limits Check

        try:
            assert spi_mode.upper() in spi_mode_list
        except AssertionError as spi_mode_err:
            print(spi_mode.upper(), "is not a defined SPI mode.")

        try:
            assert cs_mode.upper() in cs_mode_list
        except AssertionError as cs_err:
            print(cs_mode.upper(), "is not a defined CS mode.")

        try:
            assert speed_min_limit <= speed <= speed_max_limit
        except AssertionError as speed_err:
            print("Speed out of range [", speed_min_limit, speed_max_limit, "]")

        try:
            assert word_len >= bits_min_limit
        except AssertionError as bits_err:
            print("Word length must be greater than", bits_min_limit, ". Current word length:", word_len)


        # Configuring SPI

        self.tx_txt("SPI:SET:MODE {}".format(spi_mode.upper()))
        self.tx_txt("SPI:SET:CSMODE {}".format(cs_mode.upper()))
        self.tx_txt("SPI:SET:SPEED {}".format(speed))
        self.tx_txt("SPI:SET:WORD {}".format(word_len))


        self.tx_txt("SPI:SET:SET")
        print("SPI is configured")

    def spi_get_settings(
        self
    ) -> str:
        """
        Retrieves the SPI settings from Red Pitaya, prints them in console and returns
        them as an array with the following sequence:
        [mode, csmode, speed, word_len, msg_size]

        """

        # Configuring SPI

        self.tx_txt("SPI:SET:GET")
        settings = []

        settings.append(self.txrx_txt("SPI:SET:MODE?"))
        settings.append(self.txrx_txt("SPI:SET:CSMODE?"))
        settings.append(self.txrx_txt("SPI:SET:SPEED?"))
        settings.append(self.txrx_txt("SPI:SET:WORD?"))
        settings.append(self.txrx_txt("SPI:MSG:SIZE?"))


        print("SPI mode: {}".format(settings[0]))
        print("CS mode: {}".format(settings[1]))
        print("Speed: {}".format(settings[2]))
        print("Word length: {}".format(settings[3]))
        print("Message queue length: {}".format(settings[4]))

        return settings


# IEEE Mandated Commands

    def cls(self):
        """Clear Status Command"""
        return self.tx_txt('*CLS')

    def ese(self, value: int):
        """Standard Event Status Enable Command"""
        return self.tx_txt(f'*ESE {value}')

    def ese_q(self):
        """Standard Event Status Enable Query"""
        return self.txrx_txt('*ESE?')

    def esr_q(self):
        """Standard Event Status Register Query"""
        return self.txrx_txt('*ESR?')

    def idn_q(self):
        """Identification Query"""
        return self.txrx_txt('*IDN?')

    def opc(self):
        """Operation Complete Command"""
        return self.tx_txt('*OPC')

    def opc_q(self):
        """Operation Complete Query"""
        return self.txrx_txt('*OPC?')

    def rst(self):
        """Reset Command"""
        return self.tx_txt('*RST')

    def sre(self):
        """Service Request Enable Command"""
        return self.tx_txt('*SRE')

    def sre_q(self):
        """Service Request Enable Query"""
        return self.txrx_txt('*SRE?')

    def stb_q(self):
        """Read Status Byte Query"""
        return self.txrx_txt('*STB?')

# :SYSTem

    def err_c(self):
        """Error count."""
        return self.txrx_txt('SYST:ERR:COUN?')

    def err_n(self):
        """Error next."""
        return self.txrx_txt('SYST:ERR:NEXT?')