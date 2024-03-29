import {Sections} from "@/types/sections";

export class Units {
  unitName!: string
  unitDesc!: string
  unitAbout!: string
  sections!: Sections[]
  sectionsCompleted!: number
  sectionProgress!: number[]
  isComplete!: boolean
}
