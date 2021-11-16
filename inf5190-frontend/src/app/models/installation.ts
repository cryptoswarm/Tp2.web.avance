import { Arrondissement } from './arrondissement';
import { Patinoire } from './patinoire';
import { Glissade } from './glissade';
import { InstallationAquatique } from "./installation-aquatique";
export interface Installation {
  arr_name: string
  arr_cle: string
  aqua_inst: InstallationAquatique[],
  glissades: Glissade[],
  patinoires: Patinoire[]
}
