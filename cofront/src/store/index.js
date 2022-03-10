import { createStore } from 'vuex'
import theme from './modules/theme'
import user from './modules/user'

const store = createStore({
  modules: {
    theme,
    user,
  }
})

export default store;