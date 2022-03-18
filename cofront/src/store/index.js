import { createStore } from 'vuex'
import theme from './modules/theme'
import user from './modules/user'
import cache from './modules/cache'

const store = createStore({
  modules: {
    theme,
    user,
    cache,
  }
})

export default store;