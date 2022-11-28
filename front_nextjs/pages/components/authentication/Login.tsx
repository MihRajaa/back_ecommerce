import axios from 'axios';
import Image from 'next/image';
import Router from 'next/router';
import React, { useState } from 'react';

import authSlice from '../../../src/store/slices/auth';
import { useAppDispatch } from '../../../src/utils/hooks';

export default function Login() {
  const [message, setMessage] = useState('');
  const [loading, setLoading] = useState(false);
  const dispatch = useAppDispatch();

  function handleLogin(e: React.SyntheticEvent) {
    e.preventDefault();

    const target = e.target as typeof e.target & {
      username: { value: string };
      password: { value: string };
    };

    const data = {
      username: target.username.value,
      password: target.password.value,
    };

    console.log(data);

    try {
      axios
        .post('http://localhost:8000/en/dj-rest-auth/login/', data)
        .then((res) => {
          dispatch(
            authSlice.actions.setAuthTokens({
              token: res.data.access_token,
              refreshToken: res.data.refresh_token,
            })
          );
          dispatch(authSlice.actions.setAccount(res.data.user));
          setLoading(false);

          console.log('data', res.data);
          Router.push('./Profile');
        })
        .catch((err) => {
          setMessage(err);
        });
    } catch (error) {
      console.log(error);
    }
  }

  console.log('loading', loading, 'message', message);

  return (
    <div className='login-container'>
      <div className='card shadow '>
        <div className='form-signin '>
          {/* form login */}
          <form
            className='form-signin w-100 m-auto'
            method='POST'
            onSubmit={handleLogin}
            autoComplete='off'>
            {/* <Image
              className='mb-4'
              src='/docs/5.2/assets/brand/bootstrap-logo.svg'
              alt=''
              width='72'
              height='57'
            /> */}
            <h1 className='h3 mb-3 fw-normal'>Please sign in</h1>

            <div className='form-floating'>
              <input
                type='text'
                className='form-control'
                id='username'
                name='username'
                placeholder='Username'
                defaultValue=''
              />
              <label form='floatingInput'>Username</label>
            </div>
            <div className='form-floating'>
              <input
                type='password'
                className='form-control'
                id='password'
                name='password'
                placeholder='Password'
              />
              <label form='floatingPassword'>Password</label>
            </div>
            <div className='checkbox mb-3'>
              <label>
                <input type='checkbox' value='remember-me' /> Remember me
              </label>
            </div>
            <button className='btn btn-lg btn-primary' type='submit'>
              Sign in
            </button>
          </form>
        </div>

        <div className='text-center p-5'>
          <div>
            <h3>Or connect with social media</h3>
          </div>

          <div className='d-inline-flex'>
            {/* <!-- Twitter Connect --> */}
            <div className='px-1 pb-1'>
              <a className='btn btn-block btn-social btn-twitter'>
                <span className='fa fa-twitter'></span> Twitter
              </a>
            </div>
            {/* <!-- Facebook Connect --> */}
            <div className='px-1 pb-1'>
              <a href='#' className='btn btn-block btn-social btn-facebook'>
                <span className='fa fa-facebook'></span> Facebook
              </a>
            </div>
            {/* <!-- Google Connect --> */}
            <div className='px-1 pb-1'>
              <a href='#' className='btn btn-block btn-social btn-google'>
                <span className='fa fa-google-plus'></span> Google+
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
