import axios from 'axios';
import React from 'react';
import useSWR from 'swr';

import { useAppSelector } from '../../../src/utils/hooks';

const Profile = () => {
  const auth = useAppSelector((state) => state.auth);

  const user = auth.account;
  console.log('id', typeof user, user?.pk);

  axios.defaults.withCredentials = true;
  const fetcher = async (url: string) =>
    await axios
      .get(url, {
        baseURL: 'http://localhost:8000',
      })
      .then((res) => res.data);
  const { data, error } = useSWR(`/en/members/myuser/${user?.pk}/`, fetcher, {
    revalidateOnFocus: true,
    revalidateOnMount: false,
    revalidateOnReconnect: false,
    refreshWhenOffline: false,
    refreshWhenHidden: false,
    refreshInterval: 0,
  });
  console.log('data', data);

  return (
    <div className='w-full h-screen'>
      {user ? (
        <div className='w-full h-full text-center items-center'>
          <p className='self-center my-auto'>Welcome, {user.username}</p>
        </div>
      ) : (
        <p className='text-center items-center'>Loading ...</p>
      )}
    </div>
  );
};

export default Profile;
