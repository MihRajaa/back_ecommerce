import Link from 'next/link';
import { useRouter } from 'next/router';
import React from 'react';
import { TypedUseSelectorHook, useDispatch, useSelector } from 'react-redux';
import { RootState } from '../../src/store';
import authSlice from '../../src/store/slices/auth';

function Navbar() {
  const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;
  const auth = useAppSelector((state) => state.auth);

  const token = auth.token;

  const router = useRouter();

  const dispatch = useDispatch();

  const handleLogout = () => {
    dispatch(authSlice.actions.setLogout());
    router.push('./Login');
  };

  return (
    <nav
      className='navbar navbar-expand-lg sticky-top bg-black mb-3 '
      style={{ height: 50 }}>
      <div className='container-fluid mx-4'>
        <div className='collapse navbar-collapse' id='navbarTogglerDemo01'>
          <Link className='navbar-brand text-white' href=''>
            Hidden brand
          </Link>
          <ul className='navbar-nav me-auto mb-2 mb-lg-0'>
            <li className='nav-item'>
              <Link
                className='nav-link active text-white'
                aria-current='page'
                href='/components/Home'>
                Boutiques
              </Link>
            </li>
          </ul>

          {/* Login */}
          <form className=' d-flex'>
            {token ? (
              <button
                className='btn btn-sm btn-danger'
                type='button'
                onClick={handleLogout}>
                Se déconnecter
              </button>
            ) : (
              <>
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
                  onClick={() =>
                    router.push('/components/authentication/Login')
                  }>
                  Se connecter
                </button>
              </>
            )}
          </form>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
