import * as yup from 'yup';

export const contactValidationSchema = yup.object({
  name: yup.string().required('Name is required').min(2, 'Name must be at least 2 characters'),
  email: yup.string().required('Email is required').email('Email must be a valid email address'),
  phone: yup.string().required('Phone is required').matches(/^[0-9+\-() ]+$/, 'Phone number is not valid'),
  message: yup.string().required('Message is required').min(10, 'Message must be at least 10 characters'),
});
