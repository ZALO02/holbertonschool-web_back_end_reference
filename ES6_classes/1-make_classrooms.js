import ClassRoom from './0-classroom.js';

export default function initializeRooms() {
    const dimensions = [19, 20, 34];
    const result = dimensions.map((dimension) => new ClassRoom(dimension));
    return result;
}