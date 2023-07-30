import { NextResponse } from "next/server";
import { headers } from "next/headers";


export async function POST(request: Request) {

  const { imageUrl } = await request.json();

  // POST request to Replicate to start the image restoration generation process
  let startResponse = await fetch(`http://localhost:8000/generate?image_url=${imageUrl}`, {
    method: "GET",
  });

  let jsonStartResponse = await startResponse.json();

  // let endpointUrl = jsonStartResponse.image_url;

  // GET request to get the status of the image restoration process & return the result when it's ready
  // let restoredImage: string | null = null;
  // while (!restoredImage) {
  //   // Loop in 1s intervals until the alt text is ready
  //   console.log("polling for result...");
  //   let finalResponse = await fetch(endpointUrl, {
  //     method: "GET",
  //     headers: {
  //       "Content-Type": "application/json",
  //       Authorization: "Token " + process.env.REPLICATE_API_KEY,
  //     },
  //   });
  //   let jsonFinalResponse = await finalResponse.json();

  //   if (jsonFinalResponse.status === "succeeded") {
  //     restoredImage = jsonFinalResponse.output;
  //   } else if (jsonFinalResponse.status === "failed") {
  //     break;
  //   } else {
  //     await new Promise((resolve) => setTimeout(resolve, 1000));
  //   }
  // }

  // return NextResponse.json(
  //   restoredImage ? restoredImage : "Failed to restore image"
  // );

  return jsonStartResponse
}
