import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
// É nesse arquivo que a aplicação começa

// Busca o elemento root
const root = ReactDOM.createRoot(document.getElementById('root'));
// Renderiza o app. O primeiro componente que vai ser renderizado na aplicação
root.render(
  //  StrictMode é um componente que ajuda a escrever códigos mais seguros. Em proddução
  // não faz nada, mas durante o desenvolvimento ajuda a encontrar problemas na aplicação
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

