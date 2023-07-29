import Image from "next/image";
import Link from "next/link";
import Footer from "../components/Footer";
import Header from "../components/Header";
import SquigglyLines from "../components/SquigglyLines";

export default function HomePage() {
  return (
    <div className="flex max-w-6xl mx-auto flex-col items-center justify-center py-2 min-h-screen">
      <Header />
      <main className="flex flex-1 w-full flex-col items-center justify-center text-center px-4 sm:mt-20 mt-20 background-gradient">
        
        <h1 className="mx-auto max-w-4xl font-display text-5xl font-bold tracking-normal  text-gray-300 sm:text-7xl">
          Enhance MRI Models{" "}
          <span className="relative whitespace-nowrap text-blue-600">
            <SquigglyLines />
            <span className="relative">using Synthetic Lesions</span>
          </span>{" "}
          
        </h1>
        <h2 className="mx-auto mt-12 max-w-3xl text-lg sm:text-gray-400  text-gray-500 leading-7">
          Supercharge Your MRI Data with Privacy-Preserving and Lifelike Synthetic Lesions. Safely augment your datasets, simulate realistic Ischemic stroke lesions, and enhance your model accuracy effortlessly. Join us to revolutionize stroke detection and segmentation projects with state-of-the-art synthetic data.
        </h2>
        <Link
          className="bg-blue-600 rounded-xl text-white font-medium px-4 py-3 sm:mt-10 mt-8 hover:bg-blue-500 transition"
          href="/dream"
        >
          Insert Synthetic Lesions
        </Link>
        <div className="flex justify-between items-center w-full flex-col sm:mt-10 mt-6">
          <div className="flex flex-col space-y-10 mt-4 mb-16">
            <div className="flex sm:space-x-8 sm:flex-row flex-col">
              <div>
                <h3 className="mb-1 font-medium text-lg">Healthy Axial MRI Slice</h3>
                <Image
                  alt="Healthy Axial DWI Scan"
                  src="/healthy-brain-dwi.png"
                  className="w-full object-cover h-96 rounded-2xl"
                  width={400}
                  height={400}
                />
              </div>
              <div className="sm:mt-0 mt-8">
                <h3 className="mb-1 font-medium text-lg">Generated MRI with Lesion Masking</h3>
                <Image
                  alt="Generated MRI with Lesion Masking"
                  width={400}
                  height={400}
                  src="/lesion_mask_dwi.png"
                  className="w-full object-cover h-96 rounded-2xl sm:mt-0 mt-2"
                />
              </div>
            </div>
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
}
