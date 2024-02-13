export default class Currency {
  constructor(code, name) {
    if (typeof code !== 'string') {
      throw new Error('code is not a string');
    }
    this._code = code;
    
    if (typeof name !== 'string') {
      throw new Error('name is not a string');
    }
    this._name = name;
  }

  get code() {
    return this._code;
  }

  set code(code2) {
    if (typeof code2 !== 'string') {
      throw new Error('code is not a string');
    }
    this._code = code2;
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

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
