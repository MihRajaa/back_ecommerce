import axios from 'axios';
import Image from 'next/image';
import Router from 'next/router';
import React from 'react';

export default function Registration() {
  const handleSubmit = async (event: React.SyntheticEvent) => {
    event.preventDefault();

    const target = event.target as typeof event.target & {
      username: { value: string };
      email: { value: string };
      password: { value: string };
      password2: { value: string };
    };

    const data = {
      username: target.username.value,
      email: target.email.value,
      password: target.password.value,
      password2: target.password2.value,
    };

    console.log(data);

    try {
      const req = await axios.post(
        'http://localhost:8000/en/dj-rest-auth/register/',
        data
      );
      const res = req.data;
      console.log(res);

      Router.push('./Login');
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className='login-container'>
      <div className='card shadow '>
        <div className='form-signin '>
          {/* form login */}
          <form
            className='form-signin w-100 m-auto'
            method='POST'
            onSubmit={handleSubmit}>
            {/* <Image
              className='mb-4'
              src='/src/image/10861192.jpg'
              alt=''
              width='72'
              height='57'
            /> */}
            <h1 className='h3 mb-3 fw-normal'>Sign Up</h1>

            <div className='form-floating'>
              <input
                type='text'
                className='form-control'
                id='username'
                name='username'
                placeholder='Username'
              />
              <label form='floatingInput'>Username</label>
            </div>

            <div className='form-floating'>
              <input
                type='email'
                className='form-control'
                id='email'
                name='email'
                placeholder='Username'
              />
              <label form='floatingInput'>E-mail</label>
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

            <div className='form-floating'>
              <input
                type='password'
                className='form-control'
                id='password2'
                name='password2'
                placeholder='Rewrite Password'
              />
              <label form='floatingInput'>Rewrite Password</label>
            </div>

            <div className='checkbox mb-3'>
              <label>
                <input type='checkbox' value='remember-me' /> Remember me
              </label>
            </div>
            <button className='btn btn-lg btn-primary' type='submit'>
              Sign Un
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
