import { Position } from "./position";


export interface InstallationAquatique {
  id: number,
  nom_installation: string,
  type_installation?: string,
  adress?: string,
  propriete_installation?: string,
  position?: Position,
  gestion_inst?: string,
  equipement_inst?: string
  arron_id?: number
}

export class InstAquaForEdit {
  arron_id: number | undefined;
  nom_installation: string| undefined;
  type_installation: string| undefined;
  adress: string| undefined;
  propriete_installation: string| undefined;
  gestion_inst: string| undefined;
  equipement_inst: string| undefined;
  position_id: number| undefined;
}
