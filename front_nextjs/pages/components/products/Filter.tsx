import React from 'react';

function Filter() {
  return (
    <div
      className='container bg-white'
      style={{ padding: '5px', maxWidth: '800px' }}>
      <form className='row justify-content-md-center'>
        <div className='col col-lg-2 text-center'>
          <div className=''>
            <select
              className='form-select w-auto'
              id='exampleFormControlSelect2'>
              <option>Catégories</option>
              <option>1</option>
              <option>2</option>
              <option>3</option>
              <option>4</option>
              <option>5</option>
            </select>
          </div>
        </div>

        <div className='col col-lg-5 text-center'>
          <input
            type='text'
            name=''
            id=''
            className='form-control '
            placeholder='Rechercher'
            aria-describedby='helpId'
          />
        </div>

        <div className='col col-lg-2 text-center'>
          <select className='form-select w-auto' id='exampleFormControlSelect2'>
            <option>Gouvernorat</option>
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <option>5</option>
          </select>
        </div>

        <div className='col col-lg-2 text-center'>
          <button type='submit' className='btn btn-outline-primary'>
            Rechercher
            <i className='fa fa-search'></i>
          </button>
        </div>
      </form>
    </div>
  );
}

export default Filter;
