import {client, newClient} from "@/axios";

export default {
  state() {
    return {
      authToken: localStorage.authToken || '',
      user: undefined,
    };
  },
  getters: {
    user(state) {
      return state.user
    },
  },
  mutations: {
    saveUser(state, user) {
      state.user = user;
    },
    setAuthToken(state, authToken) {
      state.authToken = authToken;
      localStorage.authToken = authToken;
      newClient({
        headers: authToken ? { Authorization: `Token ${authToken}` } : {},
      });
    },
  },
  actions: {
    async fetchUserData({ state, commit }) {
      if (!state.authToken) return;
      try {
        const results = await client.get("/user/");
        commit("saveUser", results.data[0]);
      } catch {
        commit('setAuthToken', '');
      }
    },
  },
};
