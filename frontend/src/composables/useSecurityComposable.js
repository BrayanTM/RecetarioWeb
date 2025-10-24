import axios from "axios";
import { ref } from "vue";
import { useAuthStore } from "@/stores/authStore";

export function useRegisterComposable() {
  const loading = ref(false);
  const error = ref(null);
  const success = ref(false);

  let sendData = async (body) => {
    loading.value = true;
    error.value = null;
    success.value = false;

    try {
      const response = await axios.post(
        `${import.meta.env.VITE_API_URL}security/register/`,
        body,
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      // Registration successful
      success.value = true;
      return {
        success: true,
        message: response.data.message || "Registration successful! Please check your email to verify your account.",
        data: response.data,
      };
    } catch (err) {
      // Handle different error scenarios
      if (err.response) {
        // Server responded with error
        const errorMessage = err.response.data.error || "Registration failed. Please try again.";
        error.value = errorMessage;

        // Map backend errors to user-friendly messages
        let userMessage = "";

        if (errorMessage.includes("Username and password are required")) {
          userMessage = "Username and password are required";
        } else if (errorMessage.includes("Email is required")) {
          userMessage = "Email is required";
        } else if (errorMessage.includes("Email already in use")) {
          userMessage = "This email is already registered. Please use a different email or try logging in.";
        } else {
          userMessage = errorMessage;
        }

        return {
          success: false,
          message: userMessage,
          error: errorMessage,
        };
      } else if (err.request) {
        // Request made but no response
        error.value = "No response from server. Please check your connection.";
        return {
          success: false,
          message: "No response from server. Please check your connection.",
        };
      } else {
        // Something else happened
        error.value = "An unexpected error occurred.";
        return {
          success: false,
          message: "An unexpected error occurred.",
        };
      }
    } finally {
      loading.value = false;
    }
  };

  return { sendData, loading, error, success };
}

export function useLoginComposable() {
  const loading = ref(false);
  const error = ref(null);
  const success = ref(false);

  let login = async (body) => {
    loading.value = true;
    error.value = null;
    success.value = false;

    try {
      const response = await axios.post(
        `${import.meta.env.VITE_API_URL}security/login/`,
        body,
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      // Login successful
      success.value = true;

      const authStore = useAuthStore();
      authStore.login(response.data);

      return {
        success: true,
        message: "Login successful!",
        data: response.data,
      };
    } catch (err) {
      // Handle different error scenarios
      if (err.response) {
        const errorMessage = err.response.data.error || "Login failed. Please try again.";
        error.value = errorMessage;

        // Map backend errors to user-friendly messages
        let userMessage = "";

        if (errorMessage.includes("Email and password are required")) {
          userMessage = "Email and password are required";
        } else if (errorMessage.includes("Invalid credentials")) {
          userMessage = "Invalid email or password. Please try again.";
        } else if (errorMessage.includes("Account is not active")) {
          userMessage = "Your account is not active. Please verify your email first.";
        } else {
          userMessage = errorMessage;
        }

        return {
          success: false,
          message: userMessage,
          error: errorMessage,
        };
      } else if (err.request) {
        error.value = "No response from server. Please check your connection.";
        return {
          success: false,
          message: "No response from server. Please check your connection.",
        };
      } else {
        error.value = "An unexpected error occurred.";
        return {
          success: false,
          message: "An unexpected error occurred.",
        };
      }
    } finally {
      loading.value = false;
    }
  };

  return { login, loading, error, success };
}
