var cvs = document.getElementById("cvs");
var ctx = cvs.getContext("2d");
var clr = document.getElementById("clr");
var sld = document.getElementById("sld");
var upl = document.getElementById("upl");

var imageGrey = null,
    imageRainbow = null,
    originalImage = null;

function doBlue() {
	cvs.style.backgroundColor = "#D1F1FF";
	ctx.clearRect(0, 0, cvs.width, cvs.height);  // clear the canvas
  // fill text with gradient
	ctx.font = "20px Verdana";
  var gradient = ctx.createLinearGradient(0, 0, cvs.width, 0);
  gradient.addColorStop("0"," magenta");
  gradient.addColorStop("0.5", "blue");
  gradient.addColorStop("1.0", "red");
  ctx.fillStyle = gradient;
  ctx.fillText("Hello world!", 15, 30);
}

function doGrey() {
	cvs.style.backgroundColor = "#D7D9D9";
	ctx.clearRect(0, 0, cvs.width, cvs.height);  // clear the canvas
  // fill text with gradient
	ctx.font = "20px Verdana";
  var gradient = ctx.createLinearGradient(0, 0, cvs.width, 0);
  gradient.addColorStop("0"," magenta");
  gradient.addColorStop("0.5", "blue");
  gradient.addColorStop("1.0", "red");
  ctx.fillStyle = gradient;
	ctx.fillText("Bye World!", 385, 230);
}

function changeBGColor() {
  cvs.style.backgroundColor = clr.value;
}

function slide() {
	ctx.clearRect(0, 0, cvs.width, cvs.height);  // clear the canvas
	ctx.fillStyle = "#00E507";
	ctx.fillRect(parseInt(sld.value) * 0 + 10, 10, sld.value, sld.value/2);
	ctx.fillRect(parseInt(sld.value) + 20, 10, sld.value, sld.value/2);
	ctx.fillRect(parseInt(sld.value) * 2 + 30, 10, sld.value, sld.value/2);
}

function upload() {
	ctx.clearRect(0, 0, cvs.width, cvs.height);  // clear the canvas
	originalImage = new SimpleImage(upl);
	imageGrey = new SimpleImage(upl);
	imageRainbow = new SimpleImage(upl);
	originalImage.drawTo(cvs);
}

function resetImage(img=imageGrey) {
	ctx.clearRect(0, 0, cvs.width, cvs.height);
	for (var pixel of img.values()) {
		var originalPixel = originalImage.getPixel(pixel.getX(), pixel.getY());
		img.setPixel(pixel.getX(), pixel.getY(), originalPixel)
	}
	originalImage.drawTo(cvs);
}

function makeGrey() {
	if (imageGrey != null) {
    resetImage(imageGrey);
	  for (var pixel of imageGrey.values()) {
	  	var avg = (pixel.getRed() + pixel.getGreen() + pixel.getBlue()) / 3;
	  	pixel.setRed(avg);
	  	pixel.setGreen(avg);
	  	pixel.setBlue(avg);
	  }
	  imageGrey.drawTo(cvs);
	}
}

function makeRainbow() {
	resetImage(imageRainbow);
	for (var pixel of imageRainbow.values()) {
		var avg = (pixel.getRed() + pixel.getGreen() + pixel.getBlue()) / 3;

		/* ---- Red Strip ----- */
		if (pixel.getY() <= imageRainbow.getHeight() * (1/7)) {
			if (avg < 128) {
				pixel.setRed(2 * avg);
				pixel.setGreen(0);
				pixel.setBlue(0);
			} else {
				pixel.setRed(255);
				pixel.setGreen(avg * 2 - 255);
				pixel.setBlue(avg * 2 - 255);
			}
		}

		/* ----- Orange Stripe ----- */
		if (pixel.getY() > imageRainbow.getHeight() * (1/7) && pixel.getY() <= imageRainbow.getHeight() * (2/7)) {
			if (avg < 128) {
				pixel.setRed(2 * avg);
				pixel.setGreen(0.8 * avg);
				pixel.setBlue(0);
			} else {
				pixel.setRed(255);
				pixel.setGreen(1.2 * avg - 51);
				pixel.setBlue(avg * 2 - 255);
			}
		}

		/* ----- Yellow Strip ----- */
		if (pixel.getY() > imageRainbow.getHeight() * (2/7) && pixel.getY() <= imageRainbow.getHeight() * (3/7)) {
			if (avg < 128) {
				pixel.setRed(2 * avg);
				pixel.setGreen(2 * avg);
				pixel.setBlue(0);
			} else {
				pixel.setRed(255);
				pixel.setGreen(255);
				pixel.setBlue(avg * 2 - 255);
			}
		}

		/* ----- Green Strip ----- */
		if (pixel.getY() > imageRainbow.getHeight() * (3/7) && pixel.getY() <= imageRainbow.getHeight() * (4/7)) {
			if (avg < 128) {
				pixel.setRed(0);
				pixel.setGreen(2 * avg);
				pixel.setBlue(0);
			} else {
				pixel.setRed(avg * 2 - 255);
				pixel.setGreen(255);
				pixel.setBlue(avg * 2 - 255);
			}
		}

		/* ----- Blue Strip ----- */
		if (pixel.getY() > imageRainbow.getHeight() * (4/7) && pixel.getY() <= imageRainbow.getHeight() * (5/7)) {
			if (avg < 128) {
				pixel.setRed(0);
				pixel.setGreen(0);
				pixel.setBlue(2 * avg);
			} else {
				pixel.setRed(avg * 2 - 255);
				pixel.setGreen(avg * 2 - 255);
				pixel.setBlue(255);
			}
		}

		/* ----- Indigo Strip ----- */
		if (pixel.getY() > imageRainbow.getHeight() * (5/7) && pixel.getY() <= imageRainbow.getHeight() * (6/7)) {
			if (avg < 128) {
				pixel.setRed(0.8 * avg);
				pixel.setGreen(0);
				pixel.setBlue(2 * avg);
			} else {
				pixel.setRed(1.2 * avg - 51);
				pixel.setGreen(avg * 2 - 255);
				pixel.setBlue(255);
			}
		}

		/* ----- Violet Strip ----- */
		if (pixel.getY() > imageRainbow.getHeight() * (6/7) && pixel.getY() <= imageRainbow.getHeight() * (7/7)) {
			if (avg < 128) {
				pixel.setRed(1.6 * avg);
				pixel.setGreen(0);
				pixel.setBlue(1.6 * avg);
			} else {
				pixel.setRed(0.4 * avg + 153);
				pixel.setGreen(avg * 2 - 255);
				pixel.setBlue(0.4 * avg + 153);
			}
		}

	}
	imageRainbow.drawTo(cvs);
}
