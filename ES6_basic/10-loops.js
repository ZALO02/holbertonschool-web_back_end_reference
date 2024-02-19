export default function appendToEachArrayValue(array, appendString) {
	const lista = [];
  for (let idx of array) {
    lista.push(appendString + idx);
  }
  return lista;
}
