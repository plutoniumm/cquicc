export function getWeekNumber (date: Date | number | string): number {
  const d = new Date(date);
  d.setHours(0, 0, 0, 0);
  d.setDate(d.getDate() + 4 - (d.getDay() || 7));

  const yearStart: number = +new Date(d.getFullYear(), 0, 1);

  let v: number = +d - yearStart;
  v = v / 86400000 + 1

  return Math.ceil(v / 7);
};