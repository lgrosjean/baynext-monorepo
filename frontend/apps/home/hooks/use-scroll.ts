"use client"

import { useEffect, useState } from "react"

export function useScroll() {
  const [scrollY, setScrollY] = useState(0)
  const [scrollDirection, setScrollDirection] = useState<"up" | "down">("down")

  useEffect(() => {
    let lastScrollY = window.scrollY

    const updateScrollY = () => {
      const currentScrollY = window.scrollY
      setScrollDirection(currentScrollY > lastScrollY ? "down" : "up")
      setScrollY(currentScrollY)
      lastScrollY = currentScrollY
    }

    const handleScroll = () => {
      requestAnimationFrame(updateScrollY)
    }

    window.addEventListener("scroll", handleScroll, { passive: true })

    return () => {
      window.removeEventListener("scroll", handleScroll)
    }
  }, [])

  return { scrollY, scrollDirection }
}
