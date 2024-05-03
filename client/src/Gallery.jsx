import React, { useState, useEffect, use } from "react";

function Radio() {
  const [selectedOption, setSelectedOption] = useState('ColorBlack');

  const handleOptionChange = (event) => {
    setSelectedOption(event.target.value);
  };  

  return (
    <fieldset className="flex flex-wrap gap-3">
      <legend className="sr-only">Color</legend>

      <div>
        <label
          htmlFor="ColorBlack"
          className={`flex cursor-pointer items-center justify-center rounded-md border border-gray-100 bg-white px-3 py-2 text-gray-900 hover:border-gray-200 ${
            selectedOption === 'ColorBlack' && 'bg-blue-400 border-blue-500 text-white'
          }`}
        >
          <input
            type="radio"
            name="ColorOption"
            value="ColorBlack"
            id="ColorBlack"
            className="sr-only"
            checked={selectedOption === 'ColorBlack'}
            onChange={handleOptionChange}
          />
          <p className="text-sm font-medium">Erode</p>
        </label>
      </div>

      <div>
        <label
          htmlFor="ColorRed"
          className={`flex cursor-pointer items-center justify-center rounded-md border border-gray-100 bg-white px-3 py-2 text-gray-900 hover:border-gray-200 ${
            selectedOption === 'ColorRed' && 'border-blue-500 bg-blue-400 text-white'
          }`}
        >
          <input
            type="radio"
            name="ColorOption"
            value="ColorRed"
            id="ColorRed"
            className="sr-only"
            checked={selectedOption === 'ColorRed'}
            onChange={handleOptionChange}
          />
          <p className="text-sm font-medium">Dilate</p>
        </label>
      </div>

      <div>
        <label
          htmlFor="ColorBlue"
          className={`flex cursor-pointer items-center justify-center rounded-md border border-gray-100 bg-white px-3 py-2 text-gray-900 hover:border-gray-200 ${
            selectedOption === 'ColorBlue' && 'border-blue-500 bg-blue-400 text-white'
          }`}
        >
          <input
            type="radio"
            name="ColorOption"
            value="ColorBlue"
            id="ColorBlue"
            className="sr-only"
            checked={selectedOption === 'ColorBlue'}
            onChange={handleOptionChange}
          />
          <p className="text-sm font-medium">Morphological</p>
        </label>
      </div>

      <div>
        <label
          htmlFor="ColorGold"
          className={`flex cursor-pointer items-center justify-center rounded-md border border-gray-100 bg-white px-3 py-2 text-gray-900 hover:border-gray-200 ${
            selectedOption === 'ColorGold' && 'border-blue-500 bg-blue-400 text-white'
          }`}
        >
          <input
            type="radio"
            name="ColorOption"
            value="ColorGold"
            id="ColorGold"
            className="sr-only"
            checked={selectedOption === 'ColorGold'}
            onChange={handleOptionChange}
          />
          <p className="text-sm font-medium">Denoise</p>
        </label>
      </div>
    </fieldset>
  );
}

function Upload() {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    setFile(selectedFile);
    // const imageUrl = URL.createObjectURL(selectedFile);
    // setPreviewUrl(imageUrl);
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
      location.reload();
      const data = await response.json();
      console.log("Image uploaded successfully:", data); // Update images state in Gallery
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
      <Radio/>
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
  
  const [tempImages, setTempImages] = useState([]);
  const getImageData = async() =>
  {
    const response = await fetch("http://localhost:5000/image")
    const data = await response.json();
    setTempImages(data);
    console.log(data);
  }

  const handleLike = async (id) => {
    try {
      const formData = new FormData();
      formData.append('id', id); 
      const response = await fetch('http://localhost:5000/image/like', {
        method: 'POST',
        body: formData,
      });
  
      if (!response.ok) {throw new Error('Failed to like image');}
      console.log('Image liked successfully');
      location.reload();
      } catch (error) {console.error('Error liking image:', error);}
  };

  useEffect(() => {
    getImageData();
  }, []);

  return (
    <section>
      <div className="mx-auto max-w-screen-xl px-4 py-8 sm:px-6 sm:py-12 lg:px-8">
        <header className="text-center">
          <h2 className="text-xl font-bold text-gray-900 sm:text-3xl">Product Collection</h2>
        </header>

        <ul className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {/* Gallery items */}
          {/* <li>
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
          </li> */}
          {tempImages.map((image, index) => (
              <li key={index}>
              <div className="relative group">
                <a href={`http://localhost:5000/${image.image_path}`} className="block relative overflow-hidden">
                  <img
                    src={`http://localhost:5000/${image.image_path}`}
                    alt=""
                    className="h-[350px] w-full object-cover transition duration-500 group-hover:scale-105 sm:h-[450px]"
                  />
                  <div className="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition duration-300 bg-black bg-opacity-50">
                    <button className="text-white font-bold text-lg">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        className="h-6 w-6 mr-1"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth={2}
                          d="M12 21l-1.453-1.388C5.24 15.37 2 12.35 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.85-3.24 6.87-8.547 11.112L12 21z"
                        />
                      </svg>
                      {image.likes == null ? 0 : image.likes}
                    </button>
                  </div>
                </a>
                <button onClick={() => handleLike(image.id)} className="bg-red-500 text-white px-4 py-2 rounded-full absolute bottom-4 right-4">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-6 w-6"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M12 21l-1.453-1.388C5.24 15.37 2 12.35 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.85-3.24 6.87-8.547 11.112L12 21z"
                    />
                  </svg>
                </button>
              </div>
            </li>             
            
            ))}
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
