(() => {
  const episodes = {
    "tulsi-vivah": {
      title: "Tulsi Vivah",
      poster: "media/kathavachan/tulsi-vivah/poster.jpg",
      hi: {
        audio: "media/kathavachan/tulsi-vivah/tulsi-vivah-hi.mp3",
        video: "media/kathavachan/tulsi-vivah/tulsi-vivah-hi.mp4",
        captions: "media/kathavachan/tulsi-vivah/tulsi-vivah-hi.vtt"
      },
      en: {
        audio: "media/kathavachan/tulsi-vivah/tulsi-vivah-en.mp3",
        video: "media/kathavachan/tulsi-vivah/tulsi-vivah-en.mp4",
        captions: "media/kathavachan/tulsi-vivah/tulsi-vivah-en.vtt"
      }
    }
  };

  document.querySelectorAll("[data-kathavachan]").forEach((section, index) => {
    const episode = episodes[section.dataset.episode];
    if (!episode) return;

    const hindi = document.documentElement.lang === "hi";
    const id = `kathavachan-${index}`;
    const labels = hindi ? {
      intro: "तुलसी विवाह की पूरी कथा सुनें या चित्रों के साथ देखें।",
      play: "चलाएँ", pause: "रोकें", back: "10 सेकंड पीछे", forward: "10 सेकंड आगे",
      speed: "गति", fullscreen: "पूरी स्क्रीन", download: "MP3 डाउनलोड करें",
      ready: "कथा तैयार है। चलाने के लिए बटन दबाएँ।",
      loading: "कथा लोड हो रही है…", error: "मीडिया नहीं खुल सका। फिर से चलाएँ या MP3 डाउनलोड करें।",
      ended: "कथा पूरी हुई।", playing: "कथा चल रही है।", paused: "कथा रुकी हुई है।"
    } : {
      intro: "Listen to the complete story or watch the illustrated episode.",
      play: "Play", pause: "Pause", back: "Back 10 seconds", forward: "Forward 10 seconds",
      speed: "Speed", fullscreen: "Fullscreen", download: "Download MP3",
      ready: "Ready. Press play to begin.", loading: "Loading the story…",
      error: "The media could not load. Try play again or download the MP3.",
      ended: "The story has ended.", playing: "Playing the story.", paused: "Paused."
    };
    section.innerHTML = `
      <div class="katha-heading">
        <p class="katha-series">सनातन कथावाचन · Sanatana Kathavachan</p>
        <h2 id="${id}-title">${hindi ? "तुलसी विवाह की कथा" : "The story of Tulsi Vivah"}</h2>
        <p>${labels.intro}</p>
      </div>
      <div class="katha-options" role="group" aria-label="${hindi ? "भाषा और माध्यम चुनें" : "Choose language and format"}">
        <button type="button" data-format="audio" data-language="hi" lang="hi">हिन्दी में सुनें <span lang="en">Listen in Hindi</span></button>
        <button type="button" data-format="audio" data-language="en" lang="en">Listen in English</button>
        <button type="button" data-format="video" data-language="hi" lang="en">Watch in Hindi <span lang="hi">हिन्दी में देखें</span></button>
        <button type="button" data-format="video" data-language="en" lang="en">Watch in English</button>
      </div>
      <audio controls hidden preload="none" aria-label="${hindi ? "कथा का ऑडियो" : "Story audio"}"></audio>
      <video controls playsinline preload="none" hidden aria-label="${hindi ? "चित्रित कथा का वीडियो" : "Illustrated story video"}"></video>
      <div class="katha-controls">
        <button type="button" data-play>${labels.play}</button>
        <button type="button" data-seek="-10">${labels.back}</button>
        <button type="button" data-seek="10">${labels.forward}</button>
        <label for="${id}-speed">${labels.speed}
          <select id="${id}-speed"><option value="0.75">0.75×</option><option selected value="1">1×</option><option value="1.25">1.25×</option><option value="1.5">1.5×</option><option value="2">2×</option></select>
        </label>
        <button type="button" data-fullscreen hidden>${labels.fullscreen}</button>
        <a data-download download>${labels.download}</a>
      </div>
      <p class="katha-status" role="status" aria-live="polite">${labels.ready}</p>
    `;
    section.setAttribute("aria-labelledby", `${id}-title`);

    const audio = section.querySelector("audio");
    const video = section.querySelector("video");
    const speed = section.querySelector("select");
    const playButton = section.querySelector("[data-play]");
    const fullscreen = section.querySelector("[data-fullscreen]");
    const download = section.querySelector("[data-download]");
    const status = section.querySelector(".katha-status");
    const options = [...section.querySelectorAll("[data-format]")];
    let language = hindi ? "hi" : "en";
    let format = "audio";
    let active = audio;
    let selection = 0;

    const reflect = () => {
      options.forEach(button => {
        button.setAttribute("aria-pressed", String(button.dataset.language === language && button.dataset.format === format));
      });
      download.href = episode[language].audio;
    };

    const load = () => {
      active.hidden = false;
      if (active.dataset.language === language && !active.error) return;
      active.replaceChildren();
      active.src = episode[language][format];
      active.dataset.language = language;
      active.playbackRate = Number(speed.value);
      if (format === "video") {
        const track = document.createElement("track");
        track.kind = "subtitles";
        track.srclang = language;
        track.label = language === "hi" ? "हिन्दी" : "English";
        track.src = episode[language].captions;
        track.default = true;
        active.append(track);
        video.poster = episode.poster;
      }
      active.load();
    };

    options.forEach(button => button.addEventListener("click", () => {
      selection += 1;
      audio.pause();
      video.pause();
      language = button.dataset.language;
      format = button.dataset.format;
      active = format === "audio" ? audio : video;
      audio.hidden = format !== "audio";
      video.hidden = format !== "video";
      fullscreen.hidden = format !== "video";
      playButton.textContent = labels.play;
      status.textContent = labels.ready;
      reflect();
      load();
    }));

    playButton.addEventListener("click", async () => {
      load();
      if (!active.paused) {
        active.pause();
        return;
      }
      status.textContent = labels.loading;
      const attempt = selection;
      try {
        await active.play();
      } catch {
        if (attempt === selection) status.textContent = labels.error;
      }
    });
    section.querySelectorAll("[data-seek]").forEach(button => button.addEventListener("click", () => {
      if (!Number.isFinite(active.duration)) return;
      active.currentTime = Math.min(active.duration, Math.max(0, active.currentTime + Number(button.dataset.seek)));
    }));
    speed.addEventListener("change", () => {
      audio.playbackRate = Number(speed.value);
      video.playbackRate = Number(speed.value);
    });
    fullscreen.addEventListener("click", async () => {
      try {
        if (video.requestFullscreen) await video.requestFullscreen();
        else if (video.webkitEnterFullscreen) video.webkitEnterFullscreen();
      } catch {
        video.focus();
      }
    });
    [audio, video].forEach(media => {
      media.addEventListener("play", () => {
        document.querySelectorAll("[data-kathavachan] audio, [data-kathavachan] video").forEach(other => {
          if (other !== media) other.pause();
        });
        playButton.textContent = labels.pause;
        status.textContent = labels.playing;
      });
      media.addEventListener("pause", () => {
        if (media !== active) return;
        playButton.textContent = labels.play;
        status.textContent = labels.paused;
      });
      media.addEventListener("ended", () => {
        playButton.textContent = labels.play;
        status.textContent = labels.ended;
      });
      media.addEventListener("error", () => { if (media === active) status.textContent = labels.error; });
    });
    reflect();
  });
})();
