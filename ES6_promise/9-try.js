export default function guardrail(mathFunction) {
	const queue = [];
	try {
		const product = mathFunction();
		queue.push(product);
	} catch (error) {
		queue.push(`Error: ${error.message}`);
	} finally {
		queue.push('Guardrail was processed')
	};
	return queue;
};
