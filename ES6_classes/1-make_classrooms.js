import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const dimensions = [19, 20, 34];
  const result = dimensions.map((dimension) => new ClassRoom(dimension));
  return result;
}
