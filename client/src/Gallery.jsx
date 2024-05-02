import React, { useState } from "react";

function Upload() {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    setFile(selectedFile);
  };

  const handleSubmit = async () => {
    if (!file) {
      console.log("No file selected!");
      return;
    }

    const formData = new FormData();
    formData.append('user_id','1');
    formData.append("image", file);

    try {
      const response = await fetch("http://localhost:5000/image", {
        method: "POST",
        body: formData,
      });
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      console.log("Image uploaded successfully:", data);
    } catch (error) {
      console.error("Error uploading image:", error);
    }
  };

  return (
    <div className="rounded-lg bg-white p-8 shadow-2xl">
      <h2 className="text-lg font-bold">Are you sure you want to do that?</h2>

      <p className="mt-2 text-sm text-gray-500">
        Doing that could cause some issues elsewhere, are you 100% sure it's OK?
      </p>

      <div className="mt-4 flex gap-2">
        <div className="h-40 rounded-lg border-2 border-dashed flex items-center justify-center">
          <label htmlFor="file" className="cursor-pointer text-center p-4 md:p-8">
            <svg
              className="w-10 h-10 mx-auto"
              viewBox="0 0 41 40"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M12.1667 26.6667C8.48477 26.6667 5.5 23.6819 5.5 20C5.5 16.8216 7.72428 14.1627 10.7012 13.4949C10.5695 12.9066 10.5 12.2947 10.5 11.6667C10.5 7.0643 14.231 3.33334 18.8333 3.33334C22.8655 3.33334 26.2288 6.19709 27.0003 10.0016C27.0556 10.0006 27.1111 10 27.1667 10C31.769 10 35.5 13.731 35.5 18.3333C35.5 22.3649 32.6371 25.7279 28.8333 26.5M25.5 21.6667L20.5 16.6667M20.5 16.6667L15.5 21.6667M20.5 16.6667L20.5 36.6667"
                stroke="#4F46E5"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
            <p className="mt-3 text-gray-700 max-w-xs mx-auto">
              Click to{" "}
              <span className="font-medium text-indigo-600">Upload your file</span>{" "}
              or drag and drop your file here
            </p>
          </label>
          <input id="file" type="file" className="hidden" onChange={handleFileChange} />
        </div>
      </div>

      <button onClick={handleSubmit} className="mt-4 bg-indigo-500 hover:bg-indigo-600 text-white px-4 py-2 rounded-md">
        Upload Image
      </button>
    </div>
  );
}


function Gallery() {
  const [showUploadModal, setShowUploadModal] = useState(false);

  const toggleUploadModal = () => {
    setShowUploadModal(!showUploadModal);
  };

  return (
    <section>
      <div className="mx-auto max-w-screen-xl px-4 py-8 sm:px-6 sm:py-12 lg:px-8">
        <header className="text-center">
          <h2 className="text-xl font-bold text-gray-900 sm:text-3xl">Product Collection</h2>
        </header>

        <ul className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {/* Gallery items */}
          <li>
              <a href="#" class="group block relative overflow-hidden">
                <img
                  src="https://images.unsplash.com/photo-1523381210434-271e8be1f52b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80"
                  alt=""
                  class="h-[350px] w-full object-cover transition duration-500 group-hover:scale-105 sm:h-[450px]"
                />
                <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition duration-300 bg-black bg-opacity-50">
                  <button class="text-white font-bold text-lg">
                    Apply Filter
                  </button>
                </div>
              </a>
          </li>
          <li>
              <a href="#" class="group block relative overflow-hidden">
                <img
                  src="https://images.unsplash.com/photo-1523381210434-271e8be1f52b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80"
                  alt=""
                  class="h-[350px] w-full object-cover transition duration-500 group-hover:scale-105 sm:h-[450px]"
                />
                <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition duration-300 bg-black bg-opacity-50">
                  <button class="text-white font-bold text-lg">
                    Apply Filter
                  </button>
                </div>
              </a>
            </li>
            <li>
              <a href="#" class="group block relative overflow-hidden">
                <img
                  src="https://images.unsplash.com/photo-1523381210434-271e8be1f52b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80"
                  alt=""
                  class="h-[350px] w-full object-cover transition duration-500 group-hover:scale-105 sm:h-[450px]"
                />
                <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition duration-300 bg-black bg-opacity-50">
                  <button class="text-white font-bold text-lg">
                    Apply Filter
                  </button>
                </div>
              </a>
            </li>
            <li>
              <a href="#" class="group block relative overflow-hidden">
                <img
                  src="https://images.unsplash.com/photo-1523381210434-271e8be1f52b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80"
                  alt=""
                  class="h-[350px] w-full object-cover transition duration-500 group-hover:scale-105 sm:h-[450px]"
                />
                <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition duration-300 bg-black bg-opacity-50">
                  <button class="text-white font-bold text-lg">
                    Apply Filter
                  </button>
                </div>
              </a>
            </li>

        </ul>
      </div>

      {/* Button to open upload modal */}
      <button onClick={toggleUploadModal} className="fixed bottom-4 right-4 bg-blue-500 text-white px-4 py-2 rounded-md">
        Upload Your Image
      </button>

      {/* Upload modal */}
      {showUploadModal && (
        <div className="fixed top-0 left-0 w-full h-full flex items-center justify-center bg-gray-800 bg-opacity-50">
          <div className="z-10 rounded-lg bg-white p-8 shadow-2xl">
            <Upload />
            <button onClick={toggleUploadModal} className="mt-4 bg-red-500 text-white px-4 py-2 rounded-md">Close</button>
          </div>
        </div>
      )}
    </section>
  );
}

export default Gallery;
