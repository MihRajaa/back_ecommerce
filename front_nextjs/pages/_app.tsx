import type { AppProps } from 'next/app';
import store, { persistor } from '../src/store';

import { Provider } from 'react-redux';
import { PersistGate } from 'redux-persist/integration/react';

import '../styles/login.css';
import '../styles/globals.css';
import '../styles/bootstrap-social.css';
import Layout from './components/Layout';

export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <Provider store={store}>
      <PersistGate persistor={persistor} loading={null}>
        <Layout>
          <Component {...pageProps} />
        </Layout>
      </PersistGate>
    </Provider>
  );
}
