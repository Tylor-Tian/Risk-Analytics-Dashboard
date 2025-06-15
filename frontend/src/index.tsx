import React, { useEffect, useState } from 'react';
import { createRoot } from 'react-dom/client';

interface Indicator {
  id: string;
  name: string;
  category: string;
}

const App = () => {
  const [indicators, setIndicators] = useState<Indicator[]>([]);

  useEffect(() => {
    fetch('/risk/indicators')
      .then((res) => res.json())
      .then(setIndicators)
      .catch(() => setIndicators([]));
  }, []);

  return (
    <div>
      <h1>Risk Analytics Dashboard</h1>
      <ul>
        {indicators.map((ind) => (
          <li key={ind.id}>{ind.name} - {ind.category}</li>
        ))}
      </ul>
    </div>
  );
};

const root = createRoot(document.getElementById('root')!);
root.render(<App />);
