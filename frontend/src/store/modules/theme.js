import { darkTheme } from "naive-ui";

export default {
  state() {
    const themes = {
      lightTheme: undefined,
      darkTheme: darkTheme,
    };
    return {
      themes,
      theme: localStorage.theme || "lightTheme",
    };
  },
  mutations: {
    setTheme(state, theme) {
      if (!theme) {
        theme = Object.keys(state.themes).filter(
          (val) => val !== state.theme
        )[0];
      }
      state.theme = theme;
      localStorage.theme = theme;
    },
  },
  getters: {
    theme(state) {
      return state.themes[state.theme];
    },
  },
  actions: {
    switchTheme({ commit }, theme = undefined) {
      commit("setTheme", theme);
    },
  },
};
