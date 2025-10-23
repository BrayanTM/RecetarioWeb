import { readonly, ref } from "vue";

export function useRecipeDetail(slug) {

  let dataRecipes = ref({});
  let error = ref(null);

  let getData = async (slug) => {

    try {
      let response = await fetch(`${import.meta.env.VITE_API_URL}recipes/slug/${slug}/`, {
        headers: {
          'Content-Type': 'application/json',
        }
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      let result = await response.json();
      dataRecipes.value = result;
    } catch (err) {
      error.value = err;
    }

  }

  getData(slug);

  return {
    dataRecipes: readonly(dataRecipes),
    error: readonly(error),
  }

}
