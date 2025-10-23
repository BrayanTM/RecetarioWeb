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
