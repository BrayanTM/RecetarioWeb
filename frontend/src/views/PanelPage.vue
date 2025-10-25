<script setup>
import FooterBase from '@/components/FooterBase.vue';
import HeaderBase from '@/components/HeaderBase.vue';
import { useRecipe, useCreateRecipe, useUpdateRecipe, useDeleteRecipe } from '@/composables/recipeComposable';
import { recipeValidationSchema, recipeUpdateValidationSchema } from '@/schemas/validationScheme';

import { Form, Field, ErrorMessage } from 'vee-validate';
import { onMounted, onUnmounted, ref } from 'vue';
import { Fancybox } from "@fancyapps/ui";
import "@fancyapps/ui/dist/fancybox/fancybox.css";

const { categories: categories } = useRecipe();

// Composable para crear recetas
const {
  error: createError,
  successMessage: createSuccess,
  createRecipe,
  clearMessages: clearCreateMessages
} = useCreateRecipe();

// Composable para actualizar recetas
const {
  error: updateError,
  successMessage: updateSuccess,
  updateRecipe,
  clearMessages: clearUpdateMessages
} = useUpdateRecipe();

// Composable para eliminar recetas
const {
  error: deleteError,
  successMessage: deleteSuccess,
  deleteRecipe,
  clearMessages: clearDeleteMessages
} = useDeleteRecipe();

let getData = ref([]);
let recipeId = ref(null);

// Variables reactivas para el formulario (dependiendo del modo)
const name = ref('');
const category = ref('0');
const time = ref('');
const description = ref('');
const image = ref('');

// Estados combinados
const isLoading = ref(false);
const recipeError = ref(null);
const recipeSuccess = ref(null);

// Fetch user's recipes
const loadUserRecipes = async () => {
  try {
    const res = await fetch(`${import.meta.env.VITE_API_URL}recipes-panel/${localStorage.getItem('authId')}/`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${localStorage.getItem('authToken')}`,
      },
    });
    getData.value = await res.json();
  } catch (error) {
    console.error('Error loading recipes:', error);
  }
};

onMounted(() => {
  loadUserRecipes();

  // Inicializar Fancybox para las imágenes
  Fancybox.bind("[data-fancybox='gallery']", {
    // Opciones de Fancybox
    Toolbar: {
      display: {
        left: ["infobar"],
        middle: [],
        right: ["slideshow", "zoom", "thumbs", "close"],
      },
    },
    Images: {
      zoom: true,
    },
  });
});

onUnmounted(() => {
  // Limpiar Fancybox cuando el componente se desmonte
  Fancybox.destroy();
});

// Form submission
const send = async () => {
  // Limpiar mensajes previos
  recipeError.value = null;
  recipeSuccess.value = null;

  if (modal_title.value === 'Create Recipe') {
    try {
      clearCreateMessages();
      const fileInput = document.querySelector('input[type=file]');
      const file = fileInput?.files[0];

      if (!file) {
        recipeError.value = 'Please select an image file.';
        return;
      }

      const formData = new FormData();
      formData.append('name', name.value);
      formData.append('category', category.value);
      formData.append('time', time.value);
      formData.append('description', description.value);
      formData.append('file', file);

      isLoading.value = true;
      await createRecipe(formData);

      recipeSuccess.value = createSuccess.value;
      recipeError.value = createError.value;

      // Clear file input
      if (fileInput) {
        fileInput.value = '';
      }

      // Reload recipes after successful creation
      setTimeout(() => {
        loadUserRecipes();
        window.location.hash = '#close';
      }, 1500);

    } catch (error) {
      console.error('Error creating recipe:', error);
      recipeError.value = createError.value;
    } finally {
      isLoading.value = false;
    }
  }

  if (modal_title.value === 'Edit Recipe') {
    try {
      clearUpdateMessages();
      const fileInput = document.querySelector('input[type=file]');
      const file = fileInput?.files[0];

      const formData = new FormData();
      formData.append('name', name.value);
      formData.append('category', category.value);
      formData.append('time', time.value);
      formData.append('description', description.value);

      // El archivo es opcional en la actualización
      if (file) {
        formData.append('file', file);
      }

      isLoading.value = true;
      await updateRecipe(formData, recipeId.value);

      recipeSuccess.value = updateSuccess.value;
      recipeError.value = updateError.value;

      // Clear file input
      if (fileInput) {
        fileInput.value = '';
      }

      // Reload recipes after successful update
      setTimeout(() => {
        loadUserRecipes();
        window.location.hash = '#close';
      }, 1500);

    } catch (error) {
      console.error('Error updating recipe:', error);
      recipeError.value = updateError.value;
    } finally {
      isLoading.value = false;
    }
  }
};

// Limpiar mensajes
const clearMessages = () => {
  recipeError.value = null;
  recipeSuccess.value = null;
  clearCreateMessages();
  clearUpdateMessages();
  clearDeleteMessages();
};

// Modal
const modal_title = ref('');
const validationSchema = ref(recipeValidationSchema);

const create = () => {
  modal_title.value = 'Create Recipe';
  recipeId.value = null;
  validationSchema.value = recipeValidationSchema;

  // Resetear formulario
  name.value = '';
  category.value = '0';
  time.value = '';
  description.value = '';
  image.value = '';

  clearMessages();
};

const edit = (model) => {
  modal_title.value = 'Edit Recipe';
  recipeId.value = model.id;
  validationSchema.value = recipeUpdateValidationSchema;

  // Cargar datos de la receta en el formulario
  name.value = model.name;
  category.value = model.category.toString();
  time.value = model.time;
  description.value = model.description;
  image.value = model.picture_url;

  clearMessages();
};

const deleteR = async (id) => {
  if (confirm('Are you sure you want to delete this recipe?')) {
    try {
      await deleteRecipe(id);
      recipeSuccess.value = deleteSuccess.value;
      recipeError.value = deleteError.value;

      // Recargar recetas después de la eliminación exitosa
      setTimeout(() => {
        loadUserRecipes();
      }, 1500);
    } catch (error) {
      console.error('Error deleting recipe:', error);
      recipeError.value = deleteError.value;
    }
  }
};

</script>

<template>
  <HeaderBase />
  <div class="breadcumb-area bg-img bg-overlay mb-5" style="background-image: url(img/bg-img/breadcumb6.jpg)">
    <div class="container h-100">
      <div class="row h-100 align-items-center">
        <div class="col-12">
          <div class="breadcumb-text text-center">
            <h2>Panel</h2>
          </div>
        </div>
      </div>
    </div>
  </div>


  <div class="contact-area section-padding-0-80 mt-5">
    <div class="container">
      <div class="row">
        <div class="col-12">
          <div class="section-heading">
            <h3>My published recipes</h3>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col-12">
          <div class="receipe-ratings text-right my-5">
            <a href="#modal2" @click="create()" class="btn delicious-btn"><i class="fas fa-plus"></i> Create</a>
          </div>
        </div>
        <hr />
        <div class="col-12">
          <div class="table-responsive">
            <table class="table table-bordered table-hover table-striped">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Category</th>
                  <th>Name</th>
                  <th>Time</th>
                  <th>Detail</th>
                  <th>Picture</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(data, index) in getData.recipes" :key="index">
                  <td>{{ data.id }}</td>
                  <td>{{ data['category_name'] }}</td>
                  <td>{{ data.name }}</td>
                  <td>{{ data.time }}</td>
                  <td>{{ data.description }}</td>
                  <td class="text-center">
                    <a :href="data.picture_url" data-fancybox="gallery" :data-caption="data.name" class="d-block">
                      <img :src="data.picture_url" :alt="data.name" style="width: 100px; cursor: pointer;" />
                    </a>
                  </td>
                  <td class="text-center">
                    <!-- <router-link :to="{ name: 'panelEdit', params: { id: data.id } }" title="Edit ">
                      <i class="fas fa-pen-square"></i>
                    </router-link> -->
                    &nbsp;&nbsp;
                    <a href="#modal2" title="Edit" @click="edit(data)">
                      <i class="fas fa-edit"></i>
                    </a>
                    &nbsp;&nbsp;
                    <router-link to="#" @click="deleteR(data.id)" title="Delete ">
                      <i class="fas fa-trash"></i>
                    </router-link>
                  </td>
                </tr>
              </tbody>

            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
  <FooterBase />
  <div class="modalmask" id="modal2">
    <div class="modalbox rotate">
      <a href="#close" title="Close" class="close">x</a>
      <h3>{{ modal_title }}</h3>
      <!-- Form -->
      <!-- Success Message -->
      <div v-if="recipeSuccess" class="alert alert-success alert-dismissible fade show" role="alert">
        <strong>Success!</strong> {{ recipeSuccess }}
        <button type="button" class="close" @click="clearMessages()" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>

      <!-- Error Message -->
      <div v-if="recipeError" class="alert alert-danger alert-dismissible fade show" role="alert">
        <strong>Error!</strong> {{ recipeError }}
        <button type="button" class="close" @click="clearMessages()" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <Form :validation-schema="validationSchema" @submit="send()">
        <div class="contact-form-area">
          <div class="row container">

            <div class="col-12 col-lg-12">
              <ErrorMessage name="name" class="text text-danger" />
              <Field type="text" name="name" v-model="name" class="form-control" placeholder="Name:" />
            </div>

            <div class="col-12 col-lg-12">
              <ErrorMessage name="category" class="text text-danger" />
              <Field as="select" name="category" v-model="category" class="form-control" placeholder="Category:"
                style="height: calc(2.25rem + 10px);">
                <option value="0" disabled>Select a category</option>
                <option v-for="cat in categories.categories" :key="cat.id" :value="cat.id">{{ cat.name }}</option>
              </Field>
            </div>

            <div class="col-12 col-lg-12">
              <ErrorMessage name="time" class="text text-danger" />
              <Field type="text" name="time" v-model="time" class="form-control" placeholder="Time:" />
            </div>

            <div class="col-12 col-lg-12">
              <ErrorMessage name="description" class="text text-danger" />
              <Field as="textarea" name="description" v-model="description" class="form-control"
                placeholder="Description:" />
            </div>

            <div v-if="modal_title === 'Edit Recipe'" class="col-12 col-lg-12 mb-3">
              <!-- Mostrar la imagen actual de la receta -->
              <label class="font-weight-bold">Current Picture:</label>
              <div class="mt-2">
                <a :href="image" data-fancybox="edit-gallery" :data-caption="name">
                  <img :src="image" :alt="name" style="width: 150px; cursor: pointer; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" />
                </a>
              </div>
              <small class="text-muted">Upload a new image below to replace it (optional)</small>
            </div>

            <div class="col-12 col-lg-12">
              <ErrorMessage name="picture" class="text text-danger" />
              <label v-if="modal_title === 'Create Recipe'">Recipe Image (Required):</label>
              <label v-else>New Recipe Image (Optional):</label>
              <input type="file" name="picture" id="file" class="form-control" accept="image/jpeg,image/png" />
            </div>

            <div class="col-12 text-center" v-if="!isLoading">
              <button class="btn delicious-btn mt-30" type="submit" title="Submit">
                {{ modal_title === 'Create Recipe' ? 'Create Recipe' : 'Update Recipe' }}
              </button>
            </div>
            <div class="col-12 text-center" v-if="isLoading">
              <img src="/img/img/load.gif" alt="Loading..." />
            </div>
          </div>
        </div>
      </Form>
      <!-- / Form -->
    </div>
  </div>
</template>

<style scoped>
/*Efecto*/
.modalmask {
  position: fixed;
  font-family: Arial, sans-serif;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background: rgba(0, 0, 0, 0.8);
  z-index: 99999;
  opacity: 0;
  -webkit-transition: opacity 400ms ease-in;
  -moz-transition: opacity 400ms ease-in;
  transition: opacity 400ms ease-in;
  pointer-events: none;
}

.modalmask:target {
  opacity: 1;
  pointer-events: auto;
}

/*Formato de la ventana*/
.modalbox {
  width: 600px;
  position: relative;
  padding: 5px 20px 13px 20px;
  background: #fff;
  border-radius: 3px;
  -webkit-transition: all 500ms ease-in;
  -moz-transition: all 500ms ease-in;
  transition: all 500ms ease-in;

}

/*Movimientos*/

.rotate {
  margin: 1% auto;
  -webkit-transform: scale(-5, -5);
  transform: scale(-5, -5);
}


.modalmask:target .rotate {
  transform: rotate(360deg) scale(1, 1);
  -webkit-transform: rotate(360deg) scale(1, 1);
}



/*Boton de cerrar*/
.close {
  background: #606061;
  color: #FFFFFF;
  line-height: 25px;
  position: absolute;
  right: 1px;
  text-align: center;
  top: 1px;
  width: 24px;
  text-decoration: none;
  font-weight: bold;
  border-radius: 3px;

}

.close:hover {
  background: #FAAC58;
  color: #222;
}
</style>
