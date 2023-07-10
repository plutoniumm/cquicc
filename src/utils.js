export const isTop = () => {
  try {
    return window.top === window.self;
  } catch ( e ) {
    return false;
  }
};

export const defStyles = {
  "&": {
    fontSize: "18px",
    height: "100%",
    width: "100%",
  },
}