{/*
  Heads up! 👋

  Plugins:
    - @tailwindcss/forms
*/}
import React, { useState } from 'react';

function Home (){
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await fetch('http://localhost:5000/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, email }),
      });

      if (!response.ok) {
        throw new Error('Failed to sign up');
      }

      const user = await response.json();
      console.log('User signed up successfully:', user);
      // Optionally, you can redirect to another page or show a success message
      location.href = '/gallery';
    } catch (error) {
      console.error('Error signing up:', error);
      // Handle error, show error message, etc.
    }
  };


    return (
    <div className="mx-auto max-w-screen-xl px-4 py-16 sm:px-6 lg:px-8">
    <div className="mx-auto max-w-lg">
        <h1 className="text-center text-2xl font-bold text-indigo-600 sm:text-3xl">Get started today</h1>

        {/* <p className="mx-auto mt-4 max-w-md text-center text-gray-500">
        
        </p> */}

        <form onSubmit={handleSubmit} className="mb-0 mt-6 space-y-4 rounded-lg p-4 shadow-lg sm:p-6 lg:p-8">
        <p className="text-center text-lg font-medium">Sign up now !</p>
        
        <div>
            <label htmlFor="username" className="sr-only">Password</label>

            <div className="relative">
            <input
                type="text"
                className="w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm"
                placeholder="Enter Username"
            />
            </div>
        </div>

        <div>
            <label htmlFor="email" className="sr-only">Email</label>

            <div className="relative">
            <input
                type="email"
                className="w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm"
                placeholder="Enter email"
            />

            <span className="absolute inset-y-0 end-0 grid place-content-center px-4">
                <svg
                xmlns="http://www.w3.org/2000/svg"
                className="size-4 text-gray-400"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                >
                <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207"
                />
                </svg>
            </span>
            </div>
        </div>

        <button
            type="submit"
            className="block w-full rounded-lg bg-indigo-600 px-5 py-3 text-sm font-medium text-white"
        >
            Sign up
        </button>

        <p className="text-center text-sm text-gray-500">
            Already have an account?
            <a className="underline" href="#">Sign in</a>
        </p>
        </form>
    </div>
    </div>
)}

export default Home;