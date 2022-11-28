import React from 'react';
import ListProduct from './products/ListProduct';
import Filter from './products/Filter';

function Home() {
  return (
    <div className='container'>
      <div
        className='container-fluid '
        style={{ height: 'fit-content', padding: '5px', margin: '10px' }}>
        <Filter />
      </div>
      <div>
        <ListProduct />
      </div>
    </div>
  );
}

export default Home;
