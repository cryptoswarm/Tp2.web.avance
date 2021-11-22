import { TestBed } from '@angular/core/testing';

import { GlissadeServiceService } from './glissade-service.service';

describe('GlissadeServiceService', () => {
  let service: GlissadeServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GlissadeServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
