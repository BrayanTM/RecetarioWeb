import * as yup from 'yup';

export const contactValidationSchema = yup.object({
  name: yup.string().required('Name is required').min(2, 'Name must be at least 2 characters'),
  email: yup.string().required('Email is required').email('Email must be a valid email address'),
  phone: yup.string().required('Phone is required').matches(/^[0-9+\-() ]+$/, 'Phone number is not valid'),
  message: yup.string().required('Message is required').min(10, 'Message must be at least 10 characters'),
});

export const registerValidationSchema = yup.object({
  username: yup
    .string()
    .required('Username is required')
    .min(3, 'Username must be at least 3 characters')
    .max(150, 'Username must not exceed 150 characters')
    .matches(/^[\w.@+-]+$/, 'Username can only contain letters, numbers, and @/./+/-/_ characters'),
  first_name: yup
    .string()
    .required('First Name is required')
    .min(2, 'First Name must be at least 2 characters')
    .max(150, 'First Name must not exceed 150 characters')
    .trim(),
  last_name: yup
    .string()
    .required('Last Name is required')
    .min(2, 'Last Name must be at least 2 characters')
    .max(150, 'Last Name must not exceed 150 characters')
    .trim(),
  email: yup
    .string()
    .required('Email is required')
    .email('Email must be a valid email address')
    .max(254, 'Email must not exceed 254 characters')
    .trim(),
  password: yup
    .string()
    .required('Password is required')
    .min(6, 'Password must be at least 6 characters')
    .max(128, 'Password must not exceed 128 characters'),
  password_confirm: yup
    .string()
    .oneOf([yup.ref('password'), null], 'Passwords must match')
    .required('Confirm Password is required'),
});

export const loginValidationSchema = yup.object({
  email: yup
    .string()
    .required('Email is required')
    .email('Email must be a valid email address')
    .trim(),
  password: yup
    .string()
    .required('Password is required'),
});

