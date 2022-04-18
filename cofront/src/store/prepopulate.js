import store from "./index.js"

async function prepopulateStore() {
    // prepopulate user data.
    await store.dispatch('fetchUserData');
}

export default prepopulateStore;