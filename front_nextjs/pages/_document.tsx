import Document, { Head, Html, Main, NextScript } from 'next/document';

class MyDocument extends Document {
  render() {
    return (
      <Html lang='fr'>
        <Head>
          <meta name='description' content='Saheb Thika' />
          <link
            href='https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css'
            rel='stylesheet'
            crossOrigin='anonymous'
          />
          <script
            src='https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js'
            crossOrigin='anonymous'
          />
          <script
            src='https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.min.js'
            crossOrigin='anonymous'
          />
          {/* <script
            src='https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css'
            crossOrigin='anonymous'
          />
          <script
            src='https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.bundle.min.js'
            crossOrigin='anonymous'
          />
          <script
            src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js'
            crossOrigin='anonymous'
          />
          <script
            src='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.0.3/css/font-awesome.css'
            crossOrigin='anonymous'
          /> */}
        </Head>
        <body>
          <Main></Main>
          <NextScript></NextScript>
        </body>
      </Html>
    );
  }
}

export default MyDocument;
