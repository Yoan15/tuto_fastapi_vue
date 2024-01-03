import axios from "axios";

const state = {
    users: null
};

const getters = {
    isAuthenticated: state => !!state.users,
    stateUsers: state => state.users
};

const actions = {
    async register({dispatch}, form) {
        await axios.post('register', form);
        let UserForm = new FormData();
        UserForm.append('username', form.username);
        UserForm.append('password', form.password);
        await dispatch('logIn', UserForm);
    },
    async logIn({dispatch}, user) {
        await axios.post('login', user);
        await dispatch('viewMe');
    },
    async viewMe({commit}) {
        let {data} = await axios.get('users/whoami');
        await commit('setUser', data);
    },
    async deleteUser(_, id) {
        await axios.delete(`user/${id}`);
    },
    async logOut({commit}) {
        let user = null;
        commit('logout', user);
    }
};

const mutations = {
    setUser(state, user) {
        state.users = user;
    },
    logout(state, user) {
        state.users = user;
    }
};

export default {
    state,
    getters,
    actions,
    mutations
};