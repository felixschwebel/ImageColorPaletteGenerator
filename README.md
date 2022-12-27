# ImageColorPaletteGenerator
A web application for generating a color palette from an image. The user can upload an image and use the *“Get Palette”*-button to display the **10 most common colors** of that image.

<img width="866" alt="Screenshot 2022-12-27 at 21 25 08" src="https://user-images.githubusercontent.com/111788725/209718898-00d04ac9-2a18-4ca9-be50-c255c5938c39.png">

I used the **Flask framework** with **Jinja templating** to implement all the functions into the HTML code.

<img width="751" alt="Screenshot 2022-12-27 at 21 25 58" src="https://user-images.githubusercontent.com/111788725/209718911-0ce9bb72-7d40-404c-bbb9-34595e88da8d.png">

To get the colors of the image I used the **NumPy** library. The image is imported as a narray and flattened with the reshape function. 

<img width="474" alt="Screenshot 2022-12-27 at 21 26 58" src="https://user-images.githubusercontent.com/111788725/209719056-0e5a0bc5-f0a0-4aa3-8f64-3ecdffe181b9.png">

Because there are many different shades of nearly the same color, I used the histogram function with 10 bins. The indices that are returned from the histogram are used to get the RGB values. 

<img width="509" alt="Screenshot 2022-12-27 at 21 27 13" src="https://user-images.githubusercontent.com/111788725/209719074-85f8fec5-fccf-4436-826c-e29a3a4c93ce.png">

These RBG-color codes are then converted into hex-color-coding.

<img width="516" alt="Screenshot 2022-12-27 at 21 27 37" src="https://user-images.githubusercontent.com/111788725/209719098-b3d63f45-ed37-4445-a9f9-e44fe9055e3c.png">

Because I needed 2 colors in every row for my HTML frame, I converted the list into a list which contains 5 lists with 2 values each. 

<img width="521" alt="Screenshot 2022-12-27 at 21 27 26" src="https://user-images.githubusercontent.com/111788725/209719095-85974175-c77f-4eac-a365-0b37fb3f307a.png">
