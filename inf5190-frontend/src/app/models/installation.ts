import { Arrondissement } from './arrondissement';
import { Patinoire } from './patinoire';
import { Glissade } from './glissade';
import { InstallationAquatique } from "./installation-aquatique";
export interface Installation {

  arrondissement?: Arrondissement
  installations_aqua?: [InstallationAquatique],
  glissades?: [Glissade],
  patinoires?: [Patinoire]
}
