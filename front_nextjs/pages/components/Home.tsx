import React from 'react';
import ListProduct from './products/ListProduct';
import Filter from './products/Filter';

function Home() {
  return (
    <div className='container'>
      <div
        className='container-fluid d-flex bg-light'
        style={{ height: 'fit-content' }}>
        <Filter />
      </div>
      <div>
        <ListProduct />
      </div>
    </div>
  );
}

export default Home;
