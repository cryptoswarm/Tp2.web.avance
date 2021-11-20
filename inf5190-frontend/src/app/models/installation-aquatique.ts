import { Position } from "@angular/compiler";

export interface InstallationAquatique {
  id: number,
  nom_installation: string,
  type_installation?: string,
  adress?: string,
  propriete_installation?: string,
  posistion?: Position,
  gestion_inst?: string,
  equipement_inst?: string
}
