import axios from 'axios';
import createAuthRefreshInterceptor from 'axios-auth-refresh';

import store from '../store';
import authSlice from '../store/slices/auth';
import { useAppSelector } from './hooks';

const auth = useAppSelector((state) => state.auth);

const axiosService = axios.create({
  baseURL: 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json',
  },
});

// @ts-ignore
const refreshAuthLogic = async (failedRequest) => {
  const { refreshToken } = store.getState().auth;
  if (refreshToken !== null) {
    return axiosService
      .post('/api/token/refresh/', {
        refresh: refreshToken,
      })
      .then((resp) => {
        const { access, refresh } = resp.data;
        failedRequest.response.config.headers.Authorization =
          'Bearer ' + access;
        store.dispatch(
          authSlice.actions.setAuthTokens({
            token: access,
            refreshToken: refresh,
          })
        );
      })
      .catch((err) => {
        if (err.response && err.response.status === 401) {
          store.dispatch(authSlice.actions.setLogout());
        }
      });
  }
};

createAuthRefreshInterceptor(axiosService, refreshAuthLogic);

export default axiosService;
