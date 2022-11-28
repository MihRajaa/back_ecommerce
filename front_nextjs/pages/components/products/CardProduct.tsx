import Image from 'next/image';
import Link from 'next/link';
import React from 'react';

function CardProduct() {
  return (
    <div className='card p-2 shadow' style={{ width: '18rem' }}>
      {/* <Image src='/src/image/10861192.jpg' className='card-Image-top' alt='' /> */}
      <div className='card-body'>
        <h5 className='card-title'>Card title</h5>
        <p className='card-text'>
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </p>
        <Link href='#' className='btn btn-primary'>
          Go somewhere
        </Link>
      </div>
    </div>
  );
}

export default CardProduct;
