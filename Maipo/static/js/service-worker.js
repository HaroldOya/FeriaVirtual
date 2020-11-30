var cacheName = 'FeriaCache';
var filesToCache = [
    '/',
    '/js/app.js',
    '/js/menu.js',
    '/js/service-worker.js',
    '/js/formulario.js',
    '/js/jquery-3.5.1.min.js',
    '/js/letras.js',
    '/js/mostrar.js',
    '/js/formulario.js',
    'añadir_producto.html',
    'base.html',
    'cart_detail.html',
    'checkout.html',
    'export.html',
    'index.hmtl',
    'lista_producto',
    'mis_productos.html',
    'modificar_producto.hmtl',
    'subasta_apuesta.html',
    'subasta.html',
    'subastaRealizada.html',
    'registration/login.html',
    'registration/registrar_clienteEx.html',
    'registration/registrar_clienteInt.html',
    'registration/registro_productor.html',
    'registration/registro_transportista',
    'registros.html',
    '/styles/estilos.css',
    '/styles/font-awesome.css',
    '/styles/font-awesome.min.css',
    '/styles/fontello.css',
    '/styles/galery.css',
    '/styles/main.css',
    '/styles/menu.css',
    '/styles/responsivo.css',
    '/styles/subasta.css',
    '/img/correo50.png',
    '/img/face50.png',
  ];

self.addEventListener('install', function(e) {
  console.log('[ServiceWorker] Install');
  e.waitUntil(
    caches.open(cacheName).then(function(cache) {
      console.log('[ServiceWorker] Caching app shell');
      return cache.addAll(filesToCache);
    })
  );
});

self.addEventListener('activate', function(e) {
    console.log('[ServiceWorker] Activate');
});

self.addEventListener('activate', function(e) {
    console.log('[ServiceWorker] Activate');
    e.waitUntil(
      caches.keys().then(function(keyList) {
        return Promise.all(keyList.map(function(key) {
          if (key !== cacheName) {
            console.log('[ServiceWorker] Removing old cache', key);
            return caches.delete(key);
          }
        }));
      })
    );
    return self.clients.claim();
  });

  self.addEventListener('fetch', function(e) {
    console.log('[ServiceWorker] Fetch', e.request.url);
    e.respondWith(
      caches.match(e.request).then(function(response) {
        return response || fetch(e.request);
      })
    );
  });
  
  