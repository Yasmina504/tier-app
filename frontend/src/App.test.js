import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import App from '../App';

test('renders the home page', async () => {
  render(<App />);
  const linkElement = await screen.findByText(/Welcome/i);
  expect(linkElement).toBeInTheDocument();
});

