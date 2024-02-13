export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new Error('name is not a string');
    }
    this._name = name;

    if (typeof length !== 'number') {
      throw new Error('length is not a number');
    }
    this._length = length;

    if (
      !Array.isArray(students)
      || !students.every((student) => typeof student === 'string')
    ) {
      throw new Error('students must be an array of strings');
    }
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(name2) {
    if (typeof name2 !== 'string') {
      throw new Error('name is not a string');
    }
    this._name = name2;
  }

  get length() {
    return this._length;
  }

  set length(length2) {
    if (typeof length2 !== 'number') {
      throw new Error('length is not a number');
    }
    this._length = length2;
  }

  get students() {
    return this._students;
  }

  set students(students2) {
    if (
      !Array.isArray(students2)
      || !students2.every((student) => typeof student === 'string')
    ) {
      throw new Error('students must be an array of strings');
    }
    this._students = students2;
  }
}
