import { defineStore } from "pinia";

export const useAuthStore = defineStore("authStore", {
  state: () => ({
    authId: (localStorage.getItem("authId") != null) ? localStorage.getItem("authId") : null,
    authName: (localStorage.getItem("authName") != null) ? localStorage.getItem("authName") : null,
    authToken: (localStorage.getItem("authToken") != null) ? localStorage.getItem("authToken") : null,
  }),
  actions: {
    login(data) {
      localStorage.setItem("authId", data.user_id);
      localStorage.setItem("authName", data.name);
      localStorage.setItem("authToken", data.token);
    },
    isLogin() {
      if (this.authToken == null) {
        window.location.href = '/login';
      }
      this.authId = localStorage.getItem("authId");
      this.authName = localStorage.getItem("authName");
      this.authToken = localStorage.getItem("authToken");
    },
    logOut() {
      if (window.confirm("Are you sure you want to log out?")) {
        this.cerrarSesion();
      }
    },
    cerrarSesion() {
      localStorage.removeItem("authId");
      localStorage.removeItem("authName");
      localStorage.removeItem("authToken");
      this.authId = null;
      this.authName = null;
      this.authToken = null;
      window.location.href = '/login';
    },
  },
});
