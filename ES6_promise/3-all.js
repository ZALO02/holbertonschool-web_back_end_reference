import { uploadPhoto, createUser } from './utils.js'

export default function handleProfileSignup() {
	const photoProm = uploadPhoto();
	const userProm = createUser();

	return Promise.all([photoProm, userProm])
		.then(([photo, user]) => {
			console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
		})
		.catch(() => console.log('Signup system offline'));
};
