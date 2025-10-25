import { readonly, ref } from "vue";
import { useRoute } from "vue-router";

export function useRecipe() {
  let dataRecipes = ref([]);
  let categories = ref([]);
  let error = ref(null);

  let getData = async () => {
    let route = useRoute();
    let url;

    if (route.query.category_id)
    {
      url = `${import.meta.env.VITE_API_URL}recipes/search/?category_id=${route.query.category_id}&search=${route.query.search}`;
    }
    else
    {
      url = `${import.meta.env.VITE_API_URL}recipes/`;
    }

    try {
      let response = await fetch(url, {
        headers: {
          "Content-Type": "application/json",
        },
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      let result = await response.json();
      dataRecipes.value = result;
    } catch (err) {
      error.value = err;
    }
  };
  getData();

  let getCategories = async () => {
    try {
      let response = await fetch(`${import.meta.env.VITE_API_URL}categories/`, {
        headers: {
          "Content-Type": "application/json",
        },
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      let result = await response.json();
      categories.value = result;
    } catch (err) {
      error.value = err;
    }
  };
  getCategories();

  return {
    dataRecipes: readonly(dataRecipes),
    categories: readonly(categories),
    error: readonly(error),
  };
}

export function useCreateRecipe() {
  const error = ref(null);
  const successMessage = ref('');

  /**
   * Crear una nueva receta
   * @param {FormData} formData - Datos del formulario con name, category, time, description, file
   * @returns {Promise<Object>} - Promesa que resuelve con los datos de la receta creada
   */
  const createRecipe = async (formData) => {
    error.value = null;
    successMessage.value = '';

    try {
      const token = localStorage.getItem('authToken');

      if (!token) {
        throw new Error('No authentication token found. Please login.');
      }

      const response = await fetch(`${import.meta.env.VITE_API_URL}recipes/`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
        },
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        // Si hay errores de validación del backend
        if (data.errors) {
          const errorMessages = Object.entries(data.errors)
            .map(([field, messages]) => `${field}: ${messages.join(', ')}`)
            .join('\n');
          throw new Error(errorMessages);
        }
        // Si hay un mensaje de error general
        if (data.error) {
          throw new Error(data.error);
        }
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      successMessage.value = 'Recipe created successfully!';

      return data.recipe;
    } catch (err) {
      error.value = err.message || 'An error occurred while creating the recipe.';
      throw err;
    }
  };

  /**
   * Limpiar mensajes de error y éxito
   */
  const clearMessages = () => {
    error.value = null;
    successMessage.value = '';
  };

  return {
    // Estado de la operación
    error: readonly(error),
    successMessage: readonly(successMessage),

    // Métodos
    createRecipe,
    clearMessages,
  };
}

export function useUpdateRecipe() {
  const error = ref(null);
  const successMessage = ref('');

  /**
   * Actualizar una receta existente
   * @param {FormData} formData - Datos del formulario con name, category, time, description, file (opcional)
   * @param {number|string} recipeId - ID de la receta a actualizar
   * @returns {Promise<Object>} - Promesa que resuelve con los datos de la receta actualizada
   */
  const updateRecipe = async (formData, recipeId) => {
    error.value = null;
    successMessage.value = '';

    try {
      const token = localStorage.getItem('authToken');

      if (!token) {
        throw new Error('No authentication token found. Please login.');
      }

      if (!recipeId) {
        throw new Error('Recipe ID is required.');
      }

      const response = await fetch(`${import.meta.env.VITE_API_URL}recipes/${recipeId}/`, {
        method: 'PUT',
        headers: {
          'Authorization': `Bearer ${token}`,
        },
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        // Si hay errores de validación del backend
        if (data.errors) {
          const errorMessages = Object.entries(data.errors)
            .map(([field, messages]) => `${field}: ${messages.join(', ')}`)
            .join('\n');
          throw new Error(errorMessages);
        }
        // Si hay un mensaje de error general
        if (data.error) {
          throw new Error(data.error);
        }
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      successMessage.value = 'Recipe updated successfully!';

      return data.recipe;
    } catch (err) {
      error.value = err.message || 'An error occurred while updating the recipe.';
      throw err;
    }
  };

  /**
   * Limpiar mensajes de error y éxito
   */
  const clearMessages = () => {
    error.value = null;
    successMessage.value = '';
  };

  return {
    // Estado de la operación
    error: readonly(error),
    successMessage: readonly(successMessage),

    // Métodos
    updateRecipe,
    clearMessages,
  };
}

export function useDeleteRecipe() {
  const error = ref(null);
  const successMessage = ref('');

  /**
   * Eliminar una receta existente
   * @param {number|string} recipeId - ID de la receta a eliminar
   * @returns {Promise<void>} - Promesa que se resuelve cuando la receta es eliminada
   */
  const deleteRecipe = async (recipeId) => {
    error.value = null;
    successMessage.value = '';

    try {
      const token = localStorage.getItem('authToken');

      if (!token) {
        throw new Error('No authentication token found. Please login.');
      }

      if (!recipeId) {
        throw new Error('Recipe ID is required.');
      }

      const response = await fetch(`${import.meta.env.VITE_API_URL}recipes/${recipeId}/`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      successMessage.value = 'Recipe deleted successfully!';
    } catch (err) {
      error.value = err.message || 'An error occurred while deleting the recipe.';
      throw err;
    }
  };

  /**
   * Limpiar mensajes de error y éxito
   */
  const clearMessages = () => {
    error.value = null;
    successMessage.value = '';
  };

  return {
    // Estado de la operación
    error: readonly(error),
    successMessage: readonly(successMessage),

    // Métodos
    deleteRecipe,
    clearMessages,
  };
}
