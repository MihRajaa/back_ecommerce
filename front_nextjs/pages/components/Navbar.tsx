import Link from 'next/link';
import { useRouter } from 'next/router';
import React from 'react';

function Navbar() {
  const router = useRouter();

  return (
    <nav
      className='navbar navbar-expand-lg sticky-top bg-black mb-3 '
      style={{ height: 100 }}>
      <div className='container-fluid mx-4'>
        <div className='collapse navbar-collapse' id='navbarTogglerDemo01'>
          <a className='navbar-brand text-white'>Hidden brand</a>
          <ul className='navbar-nav me-auto mb-2 mb-lg-0'>
            <li className='nav-item'>
              <a
                className='nav-link active text-white'
                aria-current='page'
                href='/components/Home'>
                Home
              </a>
            </li>
          </ul>

          {/* Login */}
          <form className=' d-flex'>
            <button
              className='btn btn-success me-2'
              type='button'
              onClick={() =>
                router.push('/components/authentication/Registration')
              }>
              S'inscrire
            </button>

            <button
              className='btn btn-sm btn-danger'
              type='button'
              onClick={() => router.push('/components/authentication/Login')}>
              Se connecter
            </button>
          </form>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
